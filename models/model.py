import numpy as np
import pandas as pd  # Add this line to import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def prepare_data(df):
    df['Date'] = pd.to_datetime(df.index)  # pd refers to pandas
    df['Day'] = df['Date'].dt.dayofyear
    X = df[['Day']].values
    y = df['Close'].values
    return X, y

def train_model(df):
    """
    Train a simple linear regression model on stock data.
    """
    X, y = prepare_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_price(model, days_ahead):
    """
    Predict stock price using the trained model.
    """
    return model.predict([[days_ahead]])[0]
