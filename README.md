
# Stock Market Exploratory Data Analysis | Trend and Volatility Insights (India)

Exploratory analysis of Indian stock market data focusing on trend behavior, volatility dynamics, and return characteristics.

---

## Executive Summary

This project explores historical stock price data to understand how the market behaves over time. The analysis focuses on identifying trends, studying volatility patterns, and examining trading behavior through a time-series lens.

Rather than forcing artificial business outcomes or overcomplicating the approach, the work stays grounded in exploratory analysis. A basic forecasting model is included as an extension, while the primary focus remains on uncovering meaningful patterns in the data.

The analysis is also presented through an interactive Streamlit dashboard, allowing users to explore trends and insights visually.

---

## Analytical Objective

The objective of this project is to analyze historical stock data to better understand price behavior, identify recurring patterns, and derive insights that can support more informed financial decision-making.

---

## Stakeholders

* Retail investors
* Financial analysts
* Market researchers

---

## Methodology

The dataset was collected using the yfinance API, providing historical price and volume data.

The data was cleaned and structured for time-series analysis. Relevant time periods were selected, followed by exploratory steps including trend analysis, return calculations, rolling statistics, and volume comparison.

Visualizations were used extensively to support observations and make patterns easier to interpret.

---

## Technical Skills

| Tool / Area   | Techniques Used                      |
| ------------- | ------------------------------------ |
| Python        | Pandas (time-series analysis), NumPy |
| Visualization | Matplotlib, Seaborn, Plotly          |
| Data Source   | yfinance API                         |
| Deployment    | Streamlit                            |

---

## Visual Analysis

### Price Trend Over Time

![Price Trend](visualizations/price_trend.png)

This chart shows a clear long-term upward trajectory with intermittent sharp corrections. The noticeable drop around 2018 highlights a structural break, after which the market transitions into a new growth phase.

---

### Rolling Volatility (10-Day)

![Volatility](visualizations/rolling_volatility.png)

Volatility appears in distinct clusters rather than remaining constant. The sharp spike around 2018 indicates a period of heightened market instability, followed by gradual stabilization — supporting the idea of volatility clustering and mean reversion.

---

### Returns Distribution

![Returns](visualizations/returns_distribution.png)

The distribution is centered around zero, indicating that most daily price changes are small. However, the presence of long tails shows that extreme movements occur more frequently than expected, confirming fat-tailed behavior.

---

### Moving Averages

![Moving Average](visualizations/moving_average.png)

The moving averages closely follow the price trend while smoothing short-term noise. However, they visibly lag behind sudden price movements, reinforcing their role as confirmation indicators rather than predictive tools.

---

### Volume vs Price Relationship

![Volume vs Price](visualizations/volume_vs_price.png)

There is no strong linear relationship between volume and price. Data points are widely scattered, suggesting that price movements are influenced by multiple factors beyond trading volume alone.

---

### Cumulative Returns (Growth of ₹1)

![Cumulative Returns](visualizations/cumulative_returns.png)

Despite short-term fluctuations and drawdowns, cumulative returns show consistent long-term growth. This reinforces the presence of a sustained upward trend over time.

---

### Daily Returns Over Time

![Returns Over Time](visualizations/returns_over_time.png)

Returns fluctuate around zero with occasional sharp spikes, highlighting periods of market shocks and increased volatility.

---

## Results and Insights

Stock prices do not move in a smooth or predictable manner. Instead, they exhibit structural breaks, where sudden shifts are followed by new phases of behavior. This suggests that markets operate in distinct regimes.

Volatility appears in bursts rather than remaining constant. These bursts tend to cluster, indicating that periods of instability persist before stabilizing.

Daily returns are mostly small and centered around zero, but extreme movements occur more frequently than expected. This reflects a fat-tailed distribution and highlights higher market risk.

Volatility shows mean-reverting behavior, where spikes are followed by calmer periods.

There is also strong autocorrelation in price movements, suggesting short-term momentum effects.

Moving averages help confirm trends but lag behind actual price changes.

Volume does not show a consistent relationship with price direction, indicating that price movements are influenced by additional factors.

Despite short-term noise, cumulative returns show a consistent long-term growth trend.

---

## Recommendations (Interpretation)

* Focus on long-term trends rather than short-term fluctuations
* Be cautious during high-volatility periods
* Do not rely solely on volume for decision-making
* Use moving averages as confirmation tools rather than predictors

---

## Limitations

* Based only on historical price and volume data
* No inclusion of macroeconomic or sentiment factors
* Forecasting model is basic and experimental

---

## Next Steps

* Integrate real-time stock data
* Add sentiment analysis (news, social media)
* Apply advanced models (LSTM, ARIMA)
* Expand to multiple stocks and sectors

---

## Repository Structure

```
/data  
/notebooks  
/visualizations  
app.py  
requirements.txt  
README.md  
```

---

## Running the Project

```
git clone https://github.com/arshya5/Indian-stock-market-prediction.git  
cd Indian-stock-market-prediction  
pip install -r requirements.txt  
streamlit run app.py  
```

---

## Closing Note

This project focuses on understanding financial markets through structured analysis rather than relying solely on complex modeling. It emphasizes clarity, interpretation, and the ability to extract meaningful insights from data.

---
