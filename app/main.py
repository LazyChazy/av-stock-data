from fastapi import FastAPI, HTTPException
from .stock_data import get_stock_data
from .technical_analysis import get_technical_indicator

app = FastAPI()

@app.get("/get_stock_data")
async def stock_data(symbol: str, interval: str = "1min"):
    try:
        data = get_stock_data(symbol, interval)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/get_technical_analysis")
async def technical_analysis(symbol: str, indicator: str, period: int = 14):
    try:
        data = get_technical_indicator(symbol, indicator, period)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))