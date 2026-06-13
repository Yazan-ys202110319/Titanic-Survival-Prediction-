# Machine Learning Classification Project

## 📌 Overview
This project applies machine learning models to perform classification on a dataset.  
Two models were used and compared: Logistic Regression and Random Forest.

---

## 📊 Dataset
The dataset contains features used to predict the target variable (e.g. survival, classification label, etc.).

Main features include:
- Name (used to extract Title)
- Survived
- Age
- Sex
- Pclass
- Fare
- Embarked
- Ticket (dropped after analysis)

---

## 🛠 Feature Engineering
- Extracted **Title** from Name (Mr, Mrs, Miss, Rare, etc.)
- Grouped rare titles into a single category
- Encoded categorical variables using one-hot encoding
- Removed irrelevant features like Name and Ticket

---

## 🤖 Models Used

### 1. Logistic Regression
A linear classification model used as a baseline.

### 2. Random Forest Classifier
An ensemble model that builds multiple decision trees and averages their predictions.

---

## 📈 Model Evaluation

Both models were trained using an 80/20 train-test split.

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | 81%      |
| Random Forest       | 82%      |

(Random Forest generally performs better due to non-linear learning ability.)

---

## 🚀 How to Run

```bash
1. pip install -r requirements.txt

2. Run: main.ipynb