
import random
from topics import conversation_topics
from traits import (
    combinations, randget_schizoid_trait,
    randget_narci_trait, randget_avoid_trait)


def get_random_topic() -> str:
    n = len(conversation_topics)
    random_index = random.randint(0, n - 1)
    return conversation_topics[random_index]


def get_random_trait() -> tuple:
    """
    Returns a random combination of traits and their corresponding labels.
    The labels are in the format [schizoid, narcissistic, avoidant].
    """
    # Generate all combinations of traits
    # 0 means the trait is not present, 1 means the trait is present
    # [schizoid, narcissistic, avoidant]
    len_comb = len(combinations)
    random_index = random.randint(0, len_comb - 1)
    labels = combinations[random_index]
    traits = []
    for type_index, label in enumerate(labels):
        if label == 0:
            continue
        else:
            if type_index == 0:
                traits.append(randget_schizoid_trait())
            elif type_index == 1:
                traits.append(randget_narci_trait())
            elif type_index == 2:
                traits.append(randget_avoid_trait())
    return traits, labels


format_prompt = ("And only generate the conversation with the A: and B:" +
                 " at the beginning of each sentence, " +
                 "no other labels and boilerplate are needed," +
                 "and put the data in one line")


def generate_prompt() -> str:
    """
    Generates a prompt based on the random topic and traits.
    """
    prompt = "generate a conversation between A and B about the topic "
    prompt += get_random_topic()
    traits, labels = get_random_trait()
    prompt += f". A has the following traits: {traits}."
    prompt += format_prompt
    return prompt, labels


if __name__ == "__main__":
    # Test the functions
    print(generate_prompt())
    print(generate_prompt())
    print(generate_prompt())
    print(generate_prompt())
