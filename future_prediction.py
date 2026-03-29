import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


file = "RELIANCE.NS_features.csv"

df = pd.read_csv(file)

X = df[["Lag1", "Lag2", "Lag3"]]
y = df["Close"]

model = LinearRegression()
model.fit(X, y)

last_values = df["Close"].values[-3:].tolist()

future_prices = []

for i in range(15):

    input_data = pd.DataFrame(
        [last_values[-3:]],
        columns=["Lag1", "Lag2", "Lag3"]
    )

    next_price = model.predict(input_data)[0]

    future_prices.append(next_price)

    last_values.append(next_price)

print("Future Predictions:")

for i, price in enumerate(future_prices, start=1):
    print(f"Day {i}: {round(price, 2)}")