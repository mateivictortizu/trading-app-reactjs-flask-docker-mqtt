import yfinance as yf

if __name__ == '__main__':
    msft = yf.Ticker("BARC")
    print(msft.info)