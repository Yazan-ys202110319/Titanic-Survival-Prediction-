import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

print(data.head())

data.hist(figsize=(12, 7))
# plt.show()


# Data cleaning 

print(data.isnull().sum())
print(data.info())

print(data["Name"])


data["Age"] = data["Age"].fillna(data["Age"].mean())
print(data.tail())


data = data.drop(columns=["Cabin"])
print(data)


# feature engineering 


data['Sex'] = data['Sex'].map({'male': 1, 'female': 0})

data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

print(data.head())


print(data['Name'].apply(type).value_counts())

print(data["Name"])



# Get the title of each person
titles = []

for name in data["Name"]:
    title = name.split(",")[1].split(".")[0].strip()
    titles.append(title)

data["Title"] = titles

print(data.tail())


print(data["Title"].unique())


#  Make the rare titles into Rare 
rare_titles = ["Don", "Rev", "Dr", "Mme", "Ms", "Major", "Lady", "Sir", "Mlle", "Col", "Capt", "the Countess", "Jonkheer"] 

data["Title"] = data["Title"].replace(rare_titles, "Rare")


print(data.tail())


data = pd.get_dummies(data, columns=["Title"], drop_first=True)
print(data.head())


data = data.drop(columns='Ticket')


# To fill the Null values 
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

print(data)