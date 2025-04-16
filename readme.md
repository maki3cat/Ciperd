## Ciperd: Conversations (C) from Individuals(I) with Personality(Per) Disorders(D)

牧猫犬项目
A SYNTHETIC DATASET

<!-- 
![alt text](img/ciperd2.jpg "The 3 most popular types of personality disorders."){style="width:500px;"} -->

### Todos

#### clear part
- [ ] (dataset) keep accumulating gemini data, run diversity check
- [ ] (dataset) sft t5 as a small model for this using gemini seed data

#### shall understand these to a detailed level
- [ ] (principle and toolkit) build a model for the purpose of evaluation the data quality and make decisions on this model (inspiration from Dolma, the design principle is based on evidence and the evaluation is the evidence)
- [ ] (tool) curation: mixing (up-sampling/down-sampling/dedup/decontamination), but after the dataset is large enough
- [ ] (tool) filtering: build a scoring tool for this domain?
- [ ] (data ablation) a small model of 1B can do that 


<img src="img/ciperd2.jpg" alt="The 3 most popular types of personality disorders." width="350">

## DataSets
Progress: ▓░░░░░░░ 5% 20Million Tokens

| Name       | Explanation                                         | Number of Tokens | Size  | Number of Documents |
| ---------- | --------------------------------------------------- | ---------------- | ----- | ------------------- |
| dataset_1  | Using LLMs, prompt-v1, one prompt, hundreds of data | 170,626          | 532KB | 1800                |
| dataset_2a | LLMs, prompt-v2, format (label, prompt, data)       | 31,827           | 132KB | 100                 |
| dataset_2b | Gemini-API, prompt-v2, format (label, prompt, data) | 31,827           | 132KB | 100                 |
| dataset_3  | Using fine-tuned small LMs; (WIP)                   | \-               | \-    | \-                  |

<br>

<!-- ![alt text](img/img_diversity.jpg "Evaluation Diversity") -->

## Evaluation

### 1) Evaluation of Diversity

<img src="img/img_diversity.jpg" alt="Evaluation of Diversity." width="850">

### 2) Evaluation of Faithfulness

### 3) Evaluation of Impacts