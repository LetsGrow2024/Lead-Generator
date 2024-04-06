import yfinance as yf

def get_sp500_tickers():
    # Hardcoded list of S&P 500 tickers
    sp500_tickers = [
        'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB',  # Add more tickers as needed
        # Add more tickers here...
    ]
    return sp500_tickers

def get_high_volume_stocks(min_volume):
    # Fetch the tickers of the S&P 500 constituents
    sp500_tickers = get_sp500_tickers()

    # Define the list to store stocks with high call and put volume
    high_volume_stocks = []

    # Iterate over each stock ticker in the S&P 500
    for ticker_symbol in sp500_tickers:
        try:
            # Fetch options data for the stock ticker
            options = yf.Ticker(ticker_symbol).options

            # Calculate total call and put volume for each option contract
            total_call_volume = sum(yf.Ticker(ticker_symbol).option_chain(option_date).calls['volume'].sum() for option_date in options)
            total_put_volume = sum(yf.Ticker(ticker_symbol).option_chain(option_date).puts['volume'].sum() for option_date in options)

            # Check if both call and put volumes exceed the threshold
            if total_call_volume > min_volume and total_put_volume > min_volume:
                high_volume_stocks.append(ticker_symbol)
        except Exception as e:
            print("Error processing ticker", ticker_symbol, ":", e)

    return high_volume_stocks

# Example usage
try:
    min_volume = 1000  # Minimum volume threshold
    high_volume_stocks = get_high_volume_stocks(min_volume)
    print("Stocks with high call and put volume for options:", high_volume_stocks)
except Exception as e:
    print("An error occurred:", e)

    