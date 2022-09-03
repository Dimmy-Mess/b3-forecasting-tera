import yfinance as yf
import pandas as pd
from datetime import datetime
import os


def get_historical(stock):
    end = datetime.now()
    start = datetime(year=end.year - 30, month=end.month, day=end.day)
    path = r"../data/raw"
    assert os.path.isdir(path)
    raw = yf.Ticker("AHEB3.SA")
    print(raw)
    data = yf.download(stock, start=start, end=end)
    df = pd.DataFrame(data=data)
    print(df)
    df.to_csv(
        r"C:\Users\Fernando\Workspace\b3-forecasting-tera\App\data\raw\AHEB3.csv",
        index=False,
        sep="\t",
        header=True,
    )


data = get_historical("AHEB3.SA")
