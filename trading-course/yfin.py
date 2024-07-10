import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

'''def download_data(stock, start_date, end_date):
    data = {}
    ticker = yf.download(stock, start_date, end_date)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

if __name__ == '__main__':
    start = '2020-10-05'
    end = '2023-10-05'
    stock_data = download_data('META', start, end)
    print(stock_data)'''
  
def download_data(stock, start, end):
  data = {}
  ticker = yf.download(stock, start, end)
  data['Price'] = ticker['Adj Close']
  return pd.DataFrame(data)

def construct_signals(data, short_period, long_period):
  data['Short SMA'] = data['Price'].rolling(window=short_period).mean()
  data['Long SMA'] = data['Price'].rolling(window=long_period).mean()
  #data['Short SMA'] = data['Price'].ewm(span=short_period, adjust = False).mean()
  #data['Long SMA'] = data['Price'].ewm(span=long_period, adjust = False).mean()
  print(data)

def plot_data(data):
  plt.figure(figsize=(12,6))
  plt.plot(data['Price'], label='Stock Price', color='black')
  plt.plot(data['Short SMA'], label='Short MA', color='red')
  plt.plot(data['Long SMA'], label='Long MA', color='blue')
  plt.title('Moving average (MA) Indicators')
  plt.xlabel('Date')
  plt.ylabel('Stock Price')
  plt.show()


if __name__ == '__main__':

  start_date = datetime.datetime(2018, 1, 1)
  end_date = datetime.datetime(2023, 11, 1)

  stock_data = download_data('META', start_date, end_date)
  construct_signals(stock_data, 50, 200)
  stock_data = stock_data.dropna()
  plot_data(stock_data)
