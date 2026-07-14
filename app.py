   # Real-time FinTech Portfolio Risk & Trading Dashboard
   # P&L and return calculation engine
import yfinance as yf
import pandas as pd

# 1. Define your initial stock portfolio (Using secure Indian NSE Tickers)
portfolio_data = {
    "Ticker": ["RELIANCE.NS", "TCS.NS", "INFY.NS"],
    "Shares":[10,5,8],
    "Buy_Price": [2400.00, 3800.00, 1500.00]
}

# 2. Convert data into a structured matrix
df = pd.DataFrame(portfolio_data)

print("=== LIVE FINTECH PORTFOLIO TRADING DASHBOARD ===")
print("Fetching live data from Yahoo Finance...\n")

# Define the starting variables right before the loop begins
total_initial_value = 0
total_current_value = 0

# === THIS IS WHERE THE MATH LOOP STARTS ===
for index, row in df.iterrows():
    ticker = row["Ticker"]
    shares = row["Shares"]
    buy_price = row["Buy_Price"]
    
    # Fetch live price data safely
    stock_data = yf.Ticker(ticker)
    history = stock_data.history(period="1d")
    
    # Safe check if data fails to load
    if history.empty:
        print(f"⚠️ Error: Could not fetch data for {ticker}. Skipping...")
        continue
        
    live_price = history["Close"].iloc[-1]
    
    # Core Mathematical Equations
    initial_cost = shares * buy_price
    current_value = shares * live_price
    profit_loss = current_value - initial_cost
    return_percentage = (profit_loss / initial_cost) * 100
    
    # Running totals for your portfolio summary
    total_initial_value += initial_cost
    total_current_value += current_value
    
    # Display individual stock performance
    print(f"[{ticker}] Shares: {shares} | Buy: ₹{buy_price:.2f} | Live: ₹{live_price:.2f}")
    print(f"       P&L: ₹{profit_loss:+.2f} ({return_percentage:+.2f}%)\n")

# 4. Overall Portfolio Summary
if total_initial_value > 0:
    total_pnl = total_current_value - total_initial_value
    total_return = (total_pnl / total_initial_value) * 100

    print("="*40)
    print(f"Total Invested Capital : ₹{total_initial_value:.2f}")
    print(f"Current Portfolio Value: ₹{total_current_value:.2f}")
    print(f"Net Portfolio P&L      : ₹{total_pnl:+.2f} ({total_return:+.2f}%)")
    print("="*40)