import yfinance as yf

data = yf.download('AAPL', start='2025-04-01', end='2025-04-10')
print(data[['Close']])