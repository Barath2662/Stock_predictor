# app.py
import streamlit as st
import pandas as pd
from models.utils import download_nifty50_data, get_stock_data
from models.model import train_model, predict_price
from datetime import datetime

# Title of the app
st.title("Nifty 50 Stock Price Predictor")

# Option to download dataset
if st.button('Download Nifty 50 Stock Data'):
    st.write("Downloading stock data...")
    data = download_nifty50_data()
    st.write("Data downloaded successfully!")
    st.write(data.tail())

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

# Select stock symbol from the list
stock_symbol = st.selectbox('Select Stock', nifty50_symbols)

# Select date range for data
start_date = st.date_input('Start Date', value=datetime(2020, 1, 1))
end_date = st.date_input('End Date', value=datetime.now())

# Fetch and display stock data
if st.button('Fetch Stock Data'):
    df = get_stock_data(stock_symbol, start_date, end_date)
    st.write(df.tail())

    # Train the model
    model = train_model(df)

    # Predict next day's price
    days_ahead = (datetime.now() - datetime.combine(start_date, datetime.min.time())).days + 1


    predicted_price = predict_price(model, days_ahead)
    
    st.subheader(f"Predicted stock price for next day: ₹{predicted_price:.2f}")
