
# 📰 Fake News Classifier using Machine Learning

## 📌 Overview
This project focuses on detecting whether a news article is **real** or **fake** using Natural Language Processing (NLP) and machine learning classification techniques.

The goal is to help prevent the spread of misinformation by automatically flagging potentially fake content.

## 🧠 Techniques Used
- Text preprocessing (lowercasing, punctuation removal, stopword removal)
- Bag-of-Words and TF-IDF for feature extraction
- Classification using multiple ML models

## 📁 Dataset
- Source: [Kaggle Fake & Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- Contains two files: `Fake.csv` and `True.csv`, with labeled news articles

## 🤖 Models Used
The following machine learning classifiers were tested and compared:
- ✅ Naive Bayes
- ✅ Support Vector Machine (SVM)
- ✅ Logistic Regression
- ✅ Random Forest
- ✅ Decision Tree

## 📈 Evaluation
- Accuracy scores and confusion matrix were used for evaluation
- Best model performance was in the 90–98% accuracy range (varies by model)

## 📊 Visualizations
- Word clouds for Fake and Real articles
- Bar chart comparing model accuracies
- Confusion matrix for detailed prediction analysis

## 🛠️ How to Run
1. Clone the repository or download the files
2. Make sure required libraries are installed:
   ```bash
   pip install -r requirements.txt
