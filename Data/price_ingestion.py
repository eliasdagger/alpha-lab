import os
from typing import List
import yfinance as yf
import pandas as pd

def ingest(tickers: List[str], start_date: str, end_date: str) -> None:
    frames = []
    for t in tickers:
        try:
            data = yf.Ticker(t).history(start=start_date, end=end_date, auto_adjust=True)
            if data.empty:
                print(f"No data: {t}")
                continue
            data = data[["Close"]].reset_index()
            data["ticker"] = t
            frames.append(data)
        except Exception as e:
            print(f"Failed {t}: {e}")

    os.makedirs("data/prices", exist_ok=True)
    pd.concat(frames).to_csv("data/prices/prices.csv", index=False)

ingest(["SPY", "AAPL", "MSFT"], "2011-01-01", "2026-10-09")