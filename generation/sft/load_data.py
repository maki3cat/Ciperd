import torch
from transformers import AutoTokenizer
import os
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence
from generation import get_access_token

TOKENIZER = AutoTokenizer.from_pretrained(
    "google-t5/t5-small", token=get_access_token())
INITIAL_DECODER_INPUT = TOKENIZER.get_vocab()["<extra_id_0>"]
PAD_IDX = TOKENIZER.pad_token_id


class T5Dataset(Dataset):

    def __init__(self, data_folder, split):
        self.split = split
        self.data_folder = data_folder
        self._nl = []
        self._sql = []
        self.tokenizer = TOKENIZER
        self.process_data(data_folder, split, self.tokenizer)

    def process_data(self, data_folder, split, tokenizer):
        if split == 'train' or split == 'dev':
            self._nl = load_lines(os.path.join(data_folder, '%s.nl' % split))
            self._sql = load_lines(os.path.join(data_folder, '%s.sql' % split))
            # every line is one training example
            for i in range(len(self._nl)):
                self._nl[i] = torch.tensor(
                    tokenizer.encode(self._nl[i]), dtype=torch.long)
                sql_encoded = tokenizer.encode(self._sql[i])
                sql_with_bos = [INITIAL_DECODER_INPUT] + sql_encoded
                self._sql[i] = torch.tensor(sql_with_bos, dtype=torch.long)

        if split == 'test':
            self._nl = load_lines(os.path.join(data_folder, 'test.nl'))
            for i in range(len(self._nl)):
                self._nl[i] = torch.tensor(
                    tokenizer.encode(self._nl[i]), dtype=torch.long)

    def __len__(self):
        return len(self._nl)

    def __getitem__(self, idx):
        encoder_input = self._nl[idx]
        encoder_mask = torch.ones_like(encoder_input)
        # test only return encoders and encoder masks
        if self.split == 'test':
            return (encoder_input, encoder_mask)
        decoder_input = self._sql[idx][:-1]
        decoder_target = self._sql[idx][1:]
        return (encoder_input, encoder_mask, decoder_input, decoder_target)


def normal_collate_fn(batch):
    '''
    Collation function to perform dynamic padding for training and evaluation with the
    development or validation set.

    Inputs:
        * batch (List[Any]): batch is a list of length batch_size, where each index contains what
                             the dataset __getitem__ function returns.

    Returns: To be compatible with the provided training loop, you should be returning
        * encoder_ids: The input ids of shape BxT to be fed into the T5 encoder.
        * encoder_mask: Mask of shape BxT associated with padding tokens in the encoder input
        * decoder_inputs: Decoder input ids of shape BxT' to be fed into T5 decoder.
        * decoder_targets: The target tokens with which to train the decoder (the tokens following each decoder input)
        * initial_decoder_inputs: The very first input token to be decoder (only to be used in evaluation)
    '''
    # Unpack the batch
    encoder_inputs, encoder_masks, decoder_inputs, decoder_targets = zip(
        *batch)
    # Pad sequences
    padding_value = TOKENIZER.pad_token_id
    encoder_ids = pad_sequence(
        encoder_inputs, batch_first=True, padding_value=padding_value)
    encoder_mask = pad_sequence(
        encoder_masks, batch_first=True, padding_value=0)
    decoder_ids = pad_sequence(
        decoder_inputs, batch_first=True, padding_value=padding_value)
    decoder_targets = pad_sequence(
        decoder_targets, batch_first=True, padding_value=padding_value)
    batch_size = encoder_ids.size(0)
    initial_decoder_inputs = torch.full(
        (batch_size,), INITIAL_DECODER_INPUT, dtype=torch.long)
    return (
        encoder_ids,                # Shape: BxT
        encoder_mask,               # Shape: BxT
        decoder_ids,                # Shape: BxT'
        decoder_targets,            # Shape: BxT'
        initial_decoder_inputs
    )


def test_collate_fn(batch):
    '''
    Collation function to perform dynamic padding for inference on the test set.

    Inputs:
        * batch (List[Any]): batch is a list of length batch_size, where each index contains what
                             the dataset __getitem__ function returns.

    Recommended returns: 
        * encoder_ids: The input ids of shape BxT to be fed into the T5 encoder.
        * encoder_mask: Mask of shape BxT associated with padding tokens in the encoder input
        * initial_decoder_inputs: The very first input token to be decoder (only to be used in evaluation)
    '''
    encoder_inputs, encoder_masks = zip(*batch)
    padding_value = TOKENIZER.pad_token_id
    encoder_ids = pad_sequence(
        encoder_inputs, batch_first=True, padding_value=padding_value)
    # 0 in mask means "don't attend here"
    encoder_mask = pad_sequence(
        encoder_masks, batch_first=True, padding_value=0)
    batch_size = encoder_ids.size(0)
    initial_decoder_inputs = torch.full(
        (batch_size,), INITIAL_DECODER_INPUT, dtype=torch.long)
    return encoder_ids, encoder_mask, initial_decoder_inputs


def get_dataloader(batch_size, split):
    data_folder = 'data'
    dset = T5Dataset(data_folder, split)
    shuffle = split == "train"
    collate_fn = normal_collate_fn if split != "test" else test_collate_fn

    dataloader = DataLoader(dset, batch_size=batch_size,
                            shuffle=shuffle, collate_fn=collate_fn)
    dataloader.num_batches = len(dataloader)
    print(f"Loaded {split} with {len(dataloader)} batches")
    return dataloader


def load_t5_data(batch_size, test_batch_size):
    train_loader = get_dataloader(batch_size, "train")
    dev_loader = get_dataloader(test_batch_size, "dev")
    test_loader = get_dataloader(test_batch_size, "test")
    return train_loader, dev_loader, test_loader


def load_lines(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines


def load_prompting_data(data_folder):
    dev_sql_path = os.path.join(data_folder, 'dev.sql')
    dev_nl_path = os.path.join(data_folder, 'dev.nl')
    test_sql_path = os.path.join(data_folder, 'test.nl')

    dev_x = load_lines(dev_nl_path)
    dev_y = load_lines(dev_sql_path)
    test_x = load_lines(test_sql_path)

    return [], [], dev_x, dev_y, test_x
