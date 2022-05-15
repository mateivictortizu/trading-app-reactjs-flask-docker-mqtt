import yfinance as yf

if __name__ == "__main__":
    search_stock = yf.Ticker('MSFT')
    print(search_stock.info)
