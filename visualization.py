import requests
import pandas
import matplotlib.pyplot as plt

REQUEST_URL = "https://alpha-vantage.p.rapidapi.com/query"

QUERY_STRING = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "MSFT",
    "outputsize": "compact",
    "datatype": "json"
}

HEADERS = {
    "X-RapidAPI-Key": "e73638a09cmsh6eee572608ec92fp12fc8djsnbf7695bf4ee9",
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

data = requests.get(REQUEST_URL, headers=HEADERS, params=QUERY_STRING)

# print(data.json()['Time Series (Daily)'])

dates = list(data.json()['Time Series (Daily)'].keys())
close_vals = [float(val['4. close']) for val in data.json()['Time Series (Daily)'].values()]

dates = pandas.to_datetime(dates)

data_frame = pandas.DataFrame()
data_frame['Date'] = dates
data_frame['value'] = close_vals
data_frame.set_index('Date', inplace=True)

print(data_frame.head(3))

plt.plot(data_frame.index, data_frame['value'])
plt.show()