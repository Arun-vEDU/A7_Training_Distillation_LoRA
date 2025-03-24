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

Observations
#Odd Layer Initialization performs the best overall, with the lowest training loss and highest test accuracy.
#Even Layer Initialization is a close second, making it a viable alternative.
#LoRA underperforms in this experiment and may require further optimization.

## Evaluation and Analysis
Note: I run this experiment on my PC with 1% data from the data set.

| Model Type | Training Loss | Test Set Performance |  
|------------|--------------|----------------------|
| Odd Layer   | 0.1385        | 92.30%               | 
| Even Layer    | 0.1411        | 93.74%               | 
| LoRA     | 0.1732        | 92.58%               |

## Demo video
[![Watch the video](https://img.youtube.com/vi/tpJAWBjJGdY/maxresdefault.jpg)](https://youtu.be/tpJAWBjJGdY)
