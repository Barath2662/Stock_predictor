import yfinance as yf
import pandas as pd

# List of Nifty 50 stock symbols (with .NS for NSE stocks)
nifty50_symbols = [
    'RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'HINDUNILVR.NS',
    'ICICIBANK.NS', 'KOTAKBANK.NS', 'SBIN.NS', 'BHARTIARTL.NS', 'ITC.NS',
    'ASIANPAINT.NS', 'HCLTECH.NS', 'LT.NS', 'AXISBANK.NS', 'BAJFINANCE.NS',
    'MARUTI.NS', 'HDFC.NS', 'ULTRACEMCO.NS', 'M&M.NS', 'SUNPHARMA.NS',
    'TITAN.NS', 'WIPRO.NS', 'NESTLEIND.NS', 'POWERGRID.NS', 'BAJAJFINSV.NS',
    'NTPC.NS', 'TATASTEEL.NS', 'JSWSTEEL.NS', 'GRASIM.NS', 'ADANIGREEN.NS',
    'TECHM.NS', 'CIPLA.NS', 'HINDALCO.NS', 'ONGC.NS', 'BPCL.NS', 
    'BRITANNIA.NS', 'INDUSINDBK.NS', 'DIVISLAB.NS', 'ADANIPORTS.NS',
    'TATAMOTORS.NS', 'EICHERMOT.NS', 'APOLLOHOSP.NS', 'DRREDDY.NS',
    'COALINDIA.NS', 'HEROMOTOCO.NS', 'ADANIENT.NS', 'PIDILITIND.NS',
    'SBILIFE.NS', 'BAJAJ-AUTO.NS', 'VEDL.NS'
]

# Define the date range for downloading historical data
start_date = '2020-01-01'
end_date = '2024-09-01'

# Create an empty dictionary to store data for each stock
all_data = {}

# Loop through each stock symbol and download the data
for symbol in nifty50_symbols:
    print(f"Downloading data for {symbol}...")
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    
    # Store the data in the dictionary using the stock symbol as the key
    all_data[symbol] = stock_data

# Combine all stock data into a single DataFrame
combined_df = pd.concat(all_data, axis=1)

# Save the combined data to a CSV file
combined_df.to_csv('nifty50_stock_data.csv')

print("Data download complete! Saved to 'nifty50_stock_data.csv'.")
