import yfinance as yf

msft = yf.Ticker("MSFT")

if __name__ == "__main__":
    ticker = yf.Ticker('AAPL')
    aapl_df = ticker.history(period="1y")
    a_list = list(aapl_df['Close'])
    round_to_tenths = [f"{num:.2f}" for num in a_list]
    print(round_to_tenths)