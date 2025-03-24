## Hate Speech/Toxic Comment Dataset
I have used Jigsaw Unintended Bias in Toxicity Classification dataset for this experiment. 
Link: https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data

## Compare the performance of LoRA with the Odd Layer and Even Layer initializations

Note: I run this experiment on Google co-labs with 1% data from data set.

| Model Type | Training Loss | Test Set Performance |  
|------------|--------------|----------------------|
| Odd Layer   | 0.1613      | 94.16%               | 
| Even Layer    |0.1618        | 93.74%               | 
| LoRA     | 0.1732      | 92.58%               |

# Observations
  1. Odd Layer Initialization performs the best overall, with the lowest training loss and highest test accuracy.
  2. Even Layer Initialization is a close second, making it a viable alternative.
  3. LoRA underperforms in this experiment and may require further optimization.

## Evaluation and Analysis
Note: I run this experiment on my PC with 1% data from the data set.

| Model Type | Training Loss | Test Set Performance |  
|------------|--------------|----------------------|
| Odd Layer   | 0.1385        | 92.30%               | 
| Even Layer    | 0.1411        | 93.74%               | 
| LoRA     | 0.1732        | 92.58%               |

# Performance Differences
  1. Odd layers may focus on lower-level features (e.g., syntax), while even layers capture higher-level semantics, improving generalization.
  2. Even Layer’s higher test accuracy despite slightly worse training loss suggests it avoids overfitting better.
  3. LoRA’s lower-rank adaptation might fail to retain critical information, leading to higher training loss.
# Challenges
  1. Layer Selection: Choosing optimal layers (odd vs. even) is task-dependent.
  2. Overfitting Risk: Odd Layer’s lower training loss but weaker test accuracy suggests overfitting to the limited 1% dataset.
# Proposed Improvements
  1. Layer Mixing: Combine odd and even layers to balance low-level and high-level features.
  2. Regularization: Add dropout or weight decay to mitigate overfitting, especially with limited data.
  3. Hybrid Approaches: Combine LoRA with distillation (e.g., use LoRA to fine-tune a distilled student model).
## Demo video
[![Watch the video](https://img.youtube.com/vi/tpJAWBjJGdY/maxresdefault.jpg)](https://youtu.be/tpJAWBjJGdY)
