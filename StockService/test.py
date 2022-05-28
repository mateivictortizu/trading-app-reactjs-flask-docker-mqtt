import json
import math

import pandas as pd
import yfinance as yf


def truncate(number, digits) -> float:
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def stock_data(ticker, period, interval, observation):
    ticker = yf.Ticker(ticker)
    ticker_history = ticker.history(period, interval)
    print((ticker_history[observation]))

    sf = ticker_history[observation]
    df = pd.DataFrame({'Date': sf.index, 'Values': sf.values})

    print(df)
    lista = []
    for i in range(0, len(df['Date'].tolist())):
        # [x[i].strftime("%d-%m-%Y")
        values={"x": df['Date'].tolist()[i].strftime("%d-%m-%Y"), "y": truncate(df['Values'].tolist()[i], 2)}
        lista.append(values)
    print(lista)


if __name__ == '__main__':
    stock_data('GOOGL', '6mo', '1d', 'Open')
