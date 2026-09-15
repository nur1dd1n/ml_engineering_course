import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

data = [
    {"name": "Ivan", "gender":"male", "score": 90},
    {"name": "Aida", "gender":"female", "score": 85},
    {"name": "Adina", "gender":"female", "score": 45},
    {"name": "Ruslan", "gender": "male", "score": 78},
    {"name": "Masha", "gender": "female", "score": 89},
    {"name": "Din lizhen", "gender": "male", "score": 30}
     
]

df = pd.DataFrame(data)

print(df)

df_csv = pd.read_csv("students_pandas.csv")

print(df_csv.head(5))

print(df_csv.info)

print(df_csv.describe())

mean_score = df_csv["score"].mean()

filtered_data = df_csv[df_csv["score"] > mean_score]