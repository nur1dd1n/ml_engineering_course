import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import lightgbm as lgb
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from catboost import CatBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

df = pd.read_csv("students_4_boosting.csv")

plt.scatter(df["hours"], df["passed"])
plt.xlabel("hours of study")
plt.ylabel("Passed or not")
plt.show()

print(df.head())
print(df.info())
print(df.describe())

X = df[["hours", "coffee", "absences", "age"]]
y = df["passed"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 42)


pipe_cat = Pipeline([
    ("scaler", StandardScaler()),
    ("model", CatBoostClassifier(iterations=100, learning_rate=0.05, max_depth=3, random_state=42, verbose=False))
])

pipe_xgb = Pipeline([
    ("model", XGBClassifier(n_estimators=100, learning_rate=0.05, max_depth=3))
])

pipe_lgb = Pipeline([
    ("model", lgb.LGBMClassifier(n_estimators=100, learning_rate=0.05, max_depth=3, random_state= 42, verbosity=-1))
])

pipe_grad = Pipeline([
    ("model", GradientBoostingClassifier(n_estimators=100, learning_rate=0.05, random_state=42))
])

pipe_cat.fit(X_train, y_train)
pipe_xgb.fit(X_train, y_train)
pipe_lgb.fit(X_train, y_train)
pipe_grad.fit(X_train, y_train)



new_student = [[8, 10, 0, 19]]
print(accuracy_score(y_test, pipe_cat.predict(X_test)))
print(accuracy_score(y_test, pipe_xgb.predict(X_test)))
print(accuracy_score(y_test, pipe_lgb.predict(X_test)))
print(accuracy_score(y_test, pipe_grad.predict(X_test)))
print(pipe_cat.predict(new_student))
print(pipe_xgb.predict(new_student))
print(pipe_lgb.predict(new_student))
print(pipe_grad.predict(new_student))