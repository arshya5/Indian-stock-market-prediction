import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


file = "RELIANCE.NS_features.csv"

df = pd.read_csv(file)

df["Date"] = pd.to_datetime(df["Date"])

X = df[["Lag1", "Lag2", "Lag3"]]
y = df["Close"]

model = LinearRegression()
model.fit(X, y)

last_15 = df.tail(15)

dates = last_15["Date"]
actual = last_15["Close"]

plt.figure(figsize=(10, 5))

plt.plot(dates, actual, marker="o")

plt.title("Last 15 Days Stock Price")
plt.xlabel("Date")
plt.ylabel("Price (INR)")

plt.xticks(rotation=45)
plt.grid()

plt.show()