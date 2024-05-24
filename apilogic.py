import pandas as pd
import requests
import streamlit as st



def get_screener_data(api_key: str, marketcap: int=100000000000, beta: int=1, volumemorethan: int=1000000000,
                      sector: str='Technology', exchange: str='NASDAQ', limit: int=100) -> pd.DataFrame:
    params = {
        "marketcapmorethan": "{}".format(marketcap),
        "betalessthan": "{}".format(beta),
        "volumemorethan": "{}".format(volumemorethan),
        "sector": "{}".format(sector),
        "exchange": "{}".format(exchange),
        "limit": "{}".format(limit),
        "apikey": "{}".format(api_key)
    }
    api_url = "https://financialmodelingprep.com/api/v3/stock-screener"

    response = requests.get(api_url, params=params)
    data = response.json()
    # if 'error' in data:
    #     raise ValueError(data['error'])
    
    df = pd.DataFrame(data)

    return df
