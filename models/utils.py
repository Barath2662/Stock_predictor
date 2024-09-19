# models/utils.py
import yfinance as yf
import pandas as pd

# List of Nifty 50 stock symbols
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

def download_nifty50_data(start_date='2020-01-01', end_date='2024-09-01'):
    """
    Download historical stock data for Nifty 50 companies using yfinance.
    """
    all_data = {}
    
    for symbol in nifty50_symbols:
        print(f"Downloading data for {symbol}...")
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        
        # Store each stock's data in the dictionary
        all_data[symbol] = stock_data
    
    # Combine all stock data into a single DataFrame
    combined_df = pd.concat(all_data, axis=1)
    
    # Save to CSV (optional)
    combined_df.to_csv('data/nifty50_stock_data.csv')
    
    return combined_df

def get_stock_data(symbol, start_date, end_date):
    """
    Fetch historical data for a single stock using yfinance.
    """
    return yf.download(symbol, start=start_date, end=end_date)
