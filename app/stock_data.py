import os
import requests
from dotenv import load_dotenv

load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_data(symbol: str, interval: str = "1min"):
    function = "TIME_SERIES_INTRADAY" if interval.endswith("min") else "TIME_SERIES_DAILY"
    
    params = {
        "function": function,
        "symbol": symbol,
        "interval": interval,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if "Error Message" in data:
        raise ValueError(data["Error Message"])
    
    time_series_key = f"Time Series ({interval})" if interval.endswith("min") else "Time Series (Daily)"
    
    return {
        "symbol": symbol,
        "interval": interval,
        "data": data[time_series_key]
    }