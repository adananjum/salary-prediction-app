import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

for file in os.listdir():
    if file.endswith('.csv'):
        csv_file = file
        break

print(f"Found csv: {csv_file}")

df = pd.read_csv(csv_file)
print(df.columns.tolist())

X = df.iloc[:, 0:1]
y = df.iloc[:, 1]

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("DONE! model.pkl is fixed")