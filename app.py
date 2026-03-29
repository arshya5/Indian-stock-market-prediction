import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Stock Forecast App")

st.title("Stock Market Forecasting App")

stocks = {
    "RELIANCE": "RELIANCE.NS_features.csv",
    "TCS": "TCS.NS_features.csv",
    "INFY": "INFY.NS_features.csv",
    "HDFCBANK": "HDFCBANK.NS_features.csv",
    "ICICIBANK": "ICICIBANK.NS_features.csv"
}

selected_stock = st.selectbox("Select Stock", list(stocks.keys()))
file = stocks[selected_stock]

df = pd.read_csv(file)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")


features = ["Lag1", "Lag2", "Lag3", "MA5", "MA10", "Return"]

X = df[features]
y = df["Close"]


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)


last_15 = df.tail(15)
actual_prices = last_15["Close"]
dates_actual = last_15["Date"]


dates_actual = dates_actual.dt.strftime("%d-%b")


last_row = df.iloc[-1].copy()

future_prices = []

for i in range(15):

    input_data = pd.DataFrame([last_row[features]])

    next_price = model.predict(input_data)[0]

    future_prices.append(next_price)

    
    last_row["Lag3"] = last_row["Lag2"]
    last_row["Lag2"] = last_row["Lag1"]
    last_row["Lag1"] = next_price

    last_row["MA5"] = (last_row["MA5"] * 4 + next_price) / 5
    last_row["MA10"] = (last_row["MA10"] * 9 + next_price) / 10

    last_row["Return"] = (next_price - last_row["Lag2"]) / last_row["Lag2"]

# future dates
last_date = pd.to_datetime(last_15["Date"].iloc[-1])
future_dates = pd.date_range(start=last_date, periods=16)[1:]
future_dates = future_dates.strftime("%d-%b")


st.subheader("Last 15 Days")

fig1, ax1 = plt.subplots()

ax1.plot(dates_actual, actual_prices, marker="o", color="blue")

ax1.set_title("Recent Performance")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price (INR)")

plt.xticks(rotation=45)
ax1.grid()

st.pyplot(fig1)


st.subheader("Next 15 Days Forecast")

fig2, ax2 = plt.subplots()

ax2.plot(future_dates, future_prices, marker="o", color="orange")

ax2.set_title("Future Prediction")
ax2.set_xlabel("Date")
ax2.set_ylabel("Predicted Price (INR)")

plt.xticks(rotation=45)
ax2.grid()

st.pyplot(fig2)


st.subheader(" Recommendation")

if future_prices[-1] > actual_prices.iloc[-1]:
    st.success("BUY Signal (Uptrend Expected)")
else:
    st.error("SELL Signal (Downtrend Expected)")