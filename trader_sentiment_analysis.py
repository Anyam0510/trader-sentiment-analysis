
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
trader_df = pd.read_csv("historical_data.csv")
sentiment_df = pd.read_csv("fear_greed_index.csv")

# Preprocess
sentiment_df["date"] = pd.to_datetime(sentiment_df["date"])
trader_df["trade_date"] = pd.to_datetime(trader_df["Timestamp IST"], format="%d-%m-%Y %H:%M").dt.date
trader_df["trade_date"] = pd.to_datetime(trader_df["trade_date"])

# Merge
merged_df = pd.merge(trader_df, sentiment_df[["date", "classification"]],
                     left_on="trade_date", right_on="date", how="left")

# Grouped Analysis
grouped_stats = merged_df.groupby("classification").agg(
    avg_pnl=("Closed PnL", "mean"),
    median_pnl=("Closed PnL", "median"),
    total_volume_usd=("Size USD", "sum"),
    trade_count=("Closed PnL", "count"),
    avg_trade_size_usd=("Size USD", "mean"),
    buy_ratio=("Side", lambda x: (x == "BUY").mean()),
    sell_ratio=("Side", lambda x: (x == "SELL").mean())
).reset_index().sort_values("avg_pnl", ascending=False)

print("Grouped Trader Stats by Sentiment:")
print(grouped_stats)

# Visualizations
sns.set(style="whitegrid")
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Avg PnL
sns.barplot(data=grouped_stats, x="classification", y="avg_pnl", ax=axs[0], palette="viridis")
axs[0].set_title("Average PnL by Market Sentiment")
axs[0].set_ylabel("Avg PnL ($)")
axs[0].set_xlabel("Sentiment")

# Total Volume
sns.barplot(data=grouped_stats, x="classification", y="total_volume_usd", ax=axs[1], palette="coolwarm")
axs[1].set_title("Total Trade Volume (USD) by Sentiment")
axs[1].set_ylabel("Total Volume ($)")
axs[1].set_xlabel("Sentiment")

# Buy vs Sell Ratio
axs[2].bar(grouped_stats["classification"], grouped_stats["buy_ratio"], label="Buy", color="green")
axs[2].bar(grouped_stats["classification"], grouped_stats["sell_ratio"],
           bottom=grouped_stats["buy_ratio"], label="Sell", color="red")
axs[2].set_title("Buy vs Sell Ratio by Sentiment")
axs[2].set_ylabel("Proportion")
axs[2].legend()

plt.tight_layout()
plt.show()
