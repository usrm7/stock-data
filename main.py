import yfinance as yf
import plotly.graph_objs as go

stock_ticker = input("Enter a stock ticker: ").upper()

# get the stock info
# company_info = yf.Ticker(stock_ticker).info
data = yf.download(tickers=stock_ticker, period="5y", interval="1d")

# need to convert the columns to float and reset the index of the data frame from yfinance
data = data.reset_index()
for i in ["Open", "High", "Close", "Low"]:
    data[i] = data[i].astype("float64")

fig = go.Figure(
    [
        go.Candlestick(
            x=data["Date"],
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name=f"{stock_ticker}",
            showlegend=True,
        )
    ]
)

fig.update_layout(
    title=f"{stock_ticker} Stock Chart",
    yaxis_tickprefix="$",
    yaxis_title="Price",
)
fig.show()
