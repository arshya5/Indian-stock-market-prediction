import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


stocks = [
    "RELIANCE.NS_features.csv",
    "TCS.NS_features.csv",
    "INFY.NS_features.csv",
    "HDFCBANK.NS_features.csv",
    "ICICIBANK.NS_features.csv"
]

for file in stocks:

    print("\nTraining:", file)

    df = pd.read_csv(file)

    X = df[["Lag1", "Lag2", "Lag3"]]
    y = df["Close"]

    split = int(len(df) * 0.8)

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    print("RMSE:", round(rmse, 2))