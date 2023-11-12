# My NLP Project: Amazon Book Review Analysis

Reviews are a valuable source of information that can greatly benefit marketing teams in their decision-making processes. Studying the sentiment of book reviews can help determine whether a book should be removed from sale or promoted further. This, in turn, can lead to increased sales if the analysis is conducted consistently.

#Installation

1.Clone the projects repository:
https://github.com/irapelanoro/projects.git

2.Install the dependencies:
pip install -r requirements.txt

3.Use Google collab for the deep learning project(if it does not work in Visual studio)
Don't forget to import all the repository




## 1. Select a Dataset
The dataset chosen for this project is the Amazon book review dataset, obtained from Kaggle. The specific dataset used focuses on Amazon book reviews and can be accessed at [this link](https://www.kaggle.com/datasets/tarkkaanko/amazon?rvi=1).
Dataset : amazon_books_Data

## 2. Exploratory Data Analysis → Jupyter Notebook (projet-nlp - exploratory)
Exploratory data analysis was conducted to gain insights into the dataset and determine the key areas of focus. Various visualizations were used to enhance the exploration process.

## 3. Build Your Preprocessing Pipeline → Python (preprocessing_pipeline )
Implementing an effective preprocessing pipeline is crucial to ensure that the data is appropriately prepared for subsequent stages of the analysis.

## 4. Train a Baseline Model → Jupyter Notebook (projet-nlp - Baseline)
A baseline model was trained after importing the preprocessing pipeline. This initial model served as a starting point for further experimentation and analysis.

## 5. Improve on the Baseline → Same Jupyter  Notebook (projet-nlp - Baseline)
The baseline model's results were used to identify areas for improvement. Various techniques, such as balancing classes through oversampling or subsampling, applying class weights, and conducting hyperparameter tuning via grid search, were explored to enhance the model's performance.

## 6. Use Tensorflow (or PyTorch, JAX, ...) and Train a Sequence Model → Jupyter Notebook (projet_nlp_deeplearning_ionenantsoa)
In this phase, deep learning models were employed to achieve better results. To do so you need to use google collab, it is better to use tensorflow otherwise you may have some issue to compute.


Here is a table summarizing the performance of each model you implemented:

| Model | Accuracy | Notes |
| ----- | -------- | ----- |
| Logistic Regression | 0.85 | The model had difficulty classifying negative sentiments |
| SVM | 0.85 | Similar to the logistic regression model, the classic SVM also struggled to classify negative sentiments |
| SVM with Oversampling | 1.0 | Perfect accuracy achieved, but there were concerns of overfitting |
| LSTM (Deep Learning) | 0.80 | Initial LSTM model with a single LSTM layer achieved an accuracy of 0.80 |
| LSTM with Oversampling (Deep learning)| 0.70 | Improved LSTM model with oversampling of the minority class resulted in an accuracy of 0.70, this time the model is able to classify the positive sentiment but also the negative one |

It appears that while the oversampling techniques improved the model's ability to classify both positive and negative sentiments, there were challenges such as overfitting. The LSTM model with oversampled data achieved a slightly lower accuracy, suggesting the need for further experimentation and optimization to balance accuracy and generalizability.






Sources:

website HuggingFace 
https://www.kaggle.com/code/pradeeshprabhakar/sentiment-analysis-amazon-review         
https://medium.com/@reddyyashu20/rnn-python-code-in-keras-and-pytorch-6ab842a85e15      
https://www.analyticsvidhya.com/blog/2022/02/sentiment-analysis-with-nlp-deep-learning/



Author Ionenantsoa RAPELANORO 
