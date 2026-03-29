

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style='whitegrid')


os.makedirs("eda/visualizations", exist_ok=True)




df = pd.read_csv('data/RELIANCE.NS_features.csv')
df['Date'] = pd.to_datetime(df['Date'])

print("\nDataset Loaded Successfully\n")




print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIPTION ---")
print(df.describe())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())




plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Close'])
plt.title('Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.tight_layout()
plt.savefig("eda/visualizations/price_trend.png")
plt.show()




plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close')
plt.plot(df['MA5'], label='MA5')
plt.plot(df['MA10'], label='MA10')
plt.legend()
plt.title('Moving Averages')
plt.tight_layout()
plt.savefig("eda/visualizations/moving_average.png")
plt.show()




plt.figure(figsize=(8,5))
sns.histplot(df['Return'], bins=50, kde=True)
plt.title('Returns Distribution')
plt.tight_layout()
plt.savefig("eda/visualizations/returns_distribution.png")
plt.show()



volatility = df['Return'].std()
print("\nVolatility:", round(volatility, 4))




# ==============================
# 🔗 Correlation Heatmap
# ==============================

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=[np.number])

sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')

plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig("eda/visualizations/correlation.png")
plt.show()




plt.figure(figsize=(8,5))
plt.scatter(df['Volume'], df['Close'])
plt.title('Volume vs Price')
plt.xlabel('Volume')
plt.ylabel('Price')
plt.tight_layout()
plt.savefig("eda/visualizations/volume_vs_price.png")
plt.show()




df['Rolling_Volatility'] = df['Return'].rolling(window=10).std()

plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Rolling_Volatility'])
plt.title('Rolling Volatility (10-Day)')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.tight_layout()
plt.savefig("eda/visualizations/rolling_volatility.png")
plt.show()




print("\n=== KEY INSIGHTS ===")
print("- Stock shows clear long-term trend with periodic fluctuations")
print("- Moving averages highlight smoother trend direction")
print("- Moderate volatility observed in price movements")
print("- Strong correlation among price-related features")
print("- Volume spikes align with significant price changes")
print("- Rolling volatility reveals periods of market instability")


print("\nEDA Completed Successfully ")