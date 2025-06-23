# Trader Behavior & Market Sentiment Analysis

## Overview
This project explores how Bitcoin market sentiment â€” captured via the Fear & Greed Index â€” influences trader behavior and profitability on Hyperliquid.

**Datasets Used:**
- `historical_data.csv`: Trader-level activity on Hyperliquid
- `fear_greed_index.csv`: Market sentiment (Fear/Greed) by date

---

## Key Questions
- Do traders perform better under Fear or Greed?
- Does sentiment influence trade volume and side (Buy/Sell)?
- Are there statistically significant behavior shifts?

---

## Key Findings
**Highest Avg PnL** occurred on **Extreme Greed** days ($121.20).
**Fear-based sentiment** triggered higher trading volume and a slight **buy-side bias**.
Trade behavior during **Neutral** days was more balanced, with lower profitability.
Most trades closed at breakeven (Median PnL â‰ˆ $0), suggesting small scalps or ineffective strategies.

---

## Columns Engineered
- `trade_date`: extracted from timestamps
- Sentiment label merged by date
- Grouped analysis by sentiment: avg PnL, volume, buy ratio

---

## Visualizations (see notebook):
Average PnL by Sentiment
Buy vs Sell Distribution by SentimentTrade Volume by Sentiment

---

## How to Reproduce
1. Clone this repo
2. Run `analysis.ipynb` in Jupyter or Google Colab
3. Install packages: `pandas`, `matplotlib`, `seaborn`

---

## Author
Anyam Anitha for **Junior Data Scientist** role at PrimeTrade AI
