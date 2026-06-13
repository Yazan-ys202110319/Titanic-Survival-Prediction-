import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

print(data.head())



# Data cleaning 

print(data.isnull().sum())
print(data.info())

print(data["Name"])


data["Age"] = data["Age"].fillna(data["Age"].mean())
print(data.tail())


data = data.drop(columns=["Cabin"])
print(data)


# feature engineering 
