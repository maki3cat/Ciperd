## Ciperd: Conversations (C) from Individuals(I) with Personality(Per) Disorders(D)

A SYNTHETIC DATASET

<!-- 
![alt text](img/ciperd2.jpg "The 3 most popular types of personality disorders."){style="width:500px;"} -->

### Todos

- [ ] (principle and toolkit) build a model for the purpose of evaluation the data quality and make decisions on this model (inspiration from Dolma, the design principle is based on evidence and the evaluation is the evidence)
- [ ] (dataset) according to scale law, how many tokens we need for this corpus at least? (1 million*20 = 20 mililon as minimum requirement)
- [ ] (dataset) have multiple models of different type to generate data?
- [ ] (tool) curation: mixing (up-sampling/down-sampling/dedup/decontamination), but after the dataset is large enough
- [ ] (tool) filtering: build a scoring tool for this domain?
- [ ] (data ablation) a small model of 1B can do that 


<img src="img/ciperd2.jpg" alt="The 3 most popular types of personality disorders." width="350">

## DataSets
| Name      | Explanation                                         | Number of Tokens | Size  | Number of Documents |
| --------- | --------------------------------------------------- | ---------------- | ----- | ------------------- |
| dataset_1 | Using LLMs, prompt-v1, one prompt, hundreds of data | 171,127          | 532KB | 1800                |
| dataset_2 | Using LLMs, prompt-v2, format (label, prompt, data) | 18,183           | 108K  | 80                  |
| dataset_3 | Using fine-tuned small LMs; (WIP)                   | \-               | \-    | \-                  |

<br>

<!-- ![alt text](img/img_diversity.jpg "Evaluation Diversity") -->

## Evaluation

### 1) Evaluation of Diversity

<img src="img/img_diversity.jpg" alt="Evaluation of Diversity." width="550">

### 2) Evaluation of Faithfulness

### 3) Evaluation of Impacts