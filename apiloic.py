import pandas as pd
import requests

session = requests.Session()

def get_screener_data(apikey: "e4wKUhDNvIpFAMzMbZ05gl74yADjOv3d" ,marketcap: int =100000000000,beta:int=1,volumemorethan:int=1000000000,
                      sector: str='Technology',exchange: str='NASDAQ',limit: int =100)->pd.DataFrame:
  #setting up the parameters dictionary  
    params ={
        "marketcapmorethan":"{}".format(marketcap),
        "betalessthan":"{}".format(beta),
        "volumemorethan":"{}".format(volumemorethan),
        "sector":"{}".format(sector),
        "exchange":"{}".format(exchange),
        "limit":"{}".format(limit),
        "apikey":"{}".format(apikey)
    }
    #define api url
    api_url = "https://financialmodelingprep.com/api/v3/stock-screener?apikey=e4wKUhDNvIpFAMzMbZ05gl74yADjOv3d"
    #calll the api with request and save just the data
    response = requests.get(api_url,params = params)
    data = response.json()
    
    
    if isinstance(data, list) and data: 

        df = pd.DataFrame({
            'symbol': symbols,
            'Name': names,
            'exchange': exchanges,
            'marketcap': market_caps,
            # Add more columns as needed
        })

        symbols = [entry.get('symbol') for entry in data]
        names = [entry.get('name') for entry in data]
        exchanges = [entry.get('exchangeShortName') for entry in data]
        market_caps = [entry.get('marketCapitalization') for entry in data]
        # Add more fields as needed
        
        # Create a DataFrame using the organized lists of data
        
    else:
        df = pd.DataFrame()
    return df