import pandas as pd

stocks = [
    "RELIANCE.NS.csv",
    "TCS.NS.csv",
    "INFY.NS.csv",
    "HDFCBANK.NS.csv",
    "ICICIBANK.NS.csv"
]

for file in stocks:

    print("Processing:", file)

    df = pd.read_csv(file)

   
    df["Date"] = pd.date_range(start="2015-01-01", periods=len(df))

    
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    
    df["Lag1"] = df["Close"].shift(1)
    df["Lag2"] = df["Close"].shift(2)
    df["Lag3"] = df["Close"].shift(3)

    df["MA5"] = df["Close"].rolling(5).mean()
    df["MA10"] = df["Close"].rolling(10).mean()

    df["Return"] = df["Close"].pct_change()

    df = df.dropna()

    df.to_csv(file.replace(".csv", "_features.csv"), index=False)

    print("Saved:", file.replace(".csv", "_features.csv"))

print("Feature engineering done")