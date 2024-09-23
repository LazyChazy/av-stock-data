import pandas as pd
import pandas_ta as ta
from .stock_data import get_stock_data

def get_technical_indicator(symbol: str, indicator: str, period: int = 14):
    # Fetch stock data
    stock_data = get_stock_data(symbol)
    
    # Convert to pandas DataFrame
    df = pd.DataFrame.from_dict(stock_data["data"], orient="index")
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    
    # Rename columns
    df.columns = ["open", "high", "low", "close", "volume"]
    
    # Calculate the requested indicator
    if indicator.lower() == "rsi":
        result = df.ta.rsi(close="close", length=period)
    elif indicator.lower() == "sma":
        result = df.ta.sma(close="close", length=period)
    elif indicator.lower() == "ema":
        result = df.ta.ema(close="close", length=period)
    elif indicator.lower() == "macd":
        result = df.ta.macd(close="close")
    elif indicator.lower() == "bbands":
        result = df.ta.bbands(close="close", length=period)
    else:
        raise ValueError(f"Unsupported indicator: {indicator}")
    
    return {
        "symbol": symbol,
        "indicator": indicator,
        "period": period,
        "data": result.dropna().to_dict()
    }