import yfinance as yf
import json
import requests
from bs4 import BeautifulSoup

def dollar_volatility():
        # N * Dollars per point
        return ''
def compute_N():
        # PDN = Previous days N
        # TR = Current days true range
        # N = (19 x PDN + TR) / 20
        return ''

def compute_daily_true_range():
        # H = Current high
        # L = Current low
        # PDC =  Previous days close
        # True range = Maximum(H-L, H-PDC, PDC-L)
        return ''
#Function markets - What to buy and sell
def get_markets():
        return ''
#Function position_sizing - How much to buy and sell
def position_sizing():
        return ''
#Function entries - When to buy and sell
def entries():
        return ''
#Function stops - When to get out of a losing position
def stops():
        return ''
#Function exits - When to get out of a winning position
def exits():
        return ''
#Function tactics - How to but and sell
def tactics():
        return ''

#Function to get EPS (TTM), previous close, and calculate P/E ratio for a given ticker
def get_stock_data(ticker):
    '''
    # URL of the NASDAQ website containing the list of tickers
    #base_url = 'https://www.nasdaq.com/market-activity/stocks/screener?page={}'
    base_url = 'https://www.nasdaq.com/market-activity/stocks/screener'
    # Initialize an empty list to store all tickers
    all_tickers = []

    # Specify the number of pages to scrape
    num_pages = 10  # Adjust this based on how many pages you want to fetch

    # Loop through each page
    for page in range(1, num_pages + 1):
        print(f'Fetching page {page}...')
        print(f'Fetching page {base_url.format(page)}...')
        response = requests.get(base_url.format(page), timeout=15)
        print("RESPONSE")
        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all ticker symbols on the page
            for row in soup.find_all('div', class_='symbol'):
                ticker = row.text.strip()
                all_tickers.append(ticker)
        else:
            print(f'Failed to retrieve page {page}. Status code: {response.status_code}')

    # Specify the output file name
    output_file = 'nasdaq_tickers.txt'

    # Write the tickers to the file
    with open(output_file, 'w') as f:
        for ticker in all_tickers:
            f.write(ticker + '\n')  # Write each ticker on a new line

    print(f'Total tickers fetched: {len(all_tickers)}')
    print(f'NASDAQ tickers written to {output_file}.')
    '''

    # URL of the Wikipedia page containing the S&P 500 list
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    # Fetch the page content using requests
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first table in the page that contains the list of companies
    table = soup.find('table', {'id': 'constituents'})

    # Extract all rows from the table
    rows = table.find_all('tr')

    # Initialize an empty list to store the tickers
    sp500_tickers = []

    # Iterate over the rows and extract the ticker symbols
    for row in rows[1:]:  # Skip the header row
        columns = row.find_all('td')
        if columns:
            ticker = columns[0].text.strip()  # The ticker symbol is in the first column
            sp500_tickers.append(ticker)

    # Print the first few tickers as a sample
    print(sp500_tickers[:500])  # Display the first 10 tickers

    # Specify the output file name
    output_file = 'sp500_tickers.txt'

    # Write the tickers to the file
    with open(output_file, 'w') as f:
       for ticker in sp500_tickers:
            f.write(ticker + '\n')  # Write each ticker on a new line

    print(f'S&P 500 tickers written to {output_file}.')


    print("getting stock data...")
    url = f'https://ca.finance.yahoo.com/quote/{ticker}'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'lxml')

    #Initialize values as 'TBD' in case they are not found
    eps_ttm = 'TBD'
    previous_close = 'TBD'
    pe_ratio = 'TBD'

    #Try to find EPS (TTM)
    try:
        eps_ttm = soup.find('td', {'data-test': 'EPS_RATIO-value'}).text
        print("Try to find EPS (TTM)" + eps_ttm)
    except AttributeError:
        pass

    #Try to find the previous close price
    try:
        previous_close = soup.find('td', {'data-test': 'PREV_CLOSE-value'}).text
        print("Try to find the previous close price" + previous_close)
    except AttributeError:
        pass

    #Try to calculate P/E ratio
    try:
        if eps_ttm != 'TBD' and previous_close != 'TBD':
            eps_ttm_value = float(eps_ttm)
            previous_close_value = float(previous_close)
            if eps_ttm_value != 0:
                pe_ratio = round(previous_close_value / eps_ttm_value, 2)
    except ValueError:
        pass

    return eps_ttm, previous_close, pe_ratio

#List of tickers
tickers = ['SPY', 'ARR.TO', 'ATZ.TO', 'ARX.TO', 'BLN.TO', 'BYD.TO', 'CS.TO', 'DTOL.TO', 'DND.TO', 
           'FSV.TO', 'IVN.TO', 'JWEL.TO', 'KSI.TO', 'LUN.TO', 
           'MDA.TO', 'MEG.TO', 'NXE.TO', 'PSK.TO', 'STC.TO', 'SFTC.TO', 'TOY.TO', 
           'SYZ.TO', 'TVK.TO', 'WFG.TO', 'WCP.TO', 'SHOP.TO', 'RY.TO', 'TD.TO', 
           'CNR.TO', 'ABX.TO', 'ENB.TO', 'NTR.TO', 'BCE.TO', 'SU.TO', 'MFC.TO', 
           'BAM.TO', 'CM.TO', 'MG.TO', 'CSU.TO', 'ATD.TO', 'FNV.TO', 'POW.TO', 
           'RCI-B.TO', 'OTEX.TO', 'FTS.TO', 'WN.TO', 'CP.TO', 'FM.TO', 'L.TO']

#Dictionary to store the EPS (TTM), previous close, and P/E ratio
stock_data = {}

#Loop through the tickers and get EPS (TTM), previous close, and P/E ratio
for ticker in tickers:
    eps_ttm, previous_close, pe_ratio = get_stock_data(ticker)
    stock_data[ticker] = {'EPS (TTM)': eps_ttm, 'Previous Close': previous_close, 'P/E Ratio': pe_ratio}
    print(stock_data[ticker])

    print("yfinance")
    # Fetch the data for multiple tickers
    stocks_data = yf.download(ticker, period="1y")
   # Display the data
    print(stocks_data)

    # Fetch the stock data using the Ticker method
    stock = yf.Ticker(ticker)

    # Get historical market data (for the past year in this example)
    historical_data = stock.history(period="1y")

    # Display the data
    print(historical_data)
    print("STOCK STOCK STOCK")
    print(stock)
    # List all attributes and methods of the Ticker object
    print(dir(stock))
    print(stock.info)
    print(stock.history(period='1y'))
    print(stock.dividends)

    # List all attributes and methods of the Ticker object
    attributes = dir(stock)

    # Attributes and methods to include in the JSON output
    attributes = {
       "info": stock.info,
    }
    # Convert the list into a JSON-formatted string
    #attributes_json = json.dumps(attributes, indent=4)
    attributes_json = json.dumps(attributes, indent=4, default=str)

    # Print the JSON-formatted list
    print(attributes_json)


#Print the results
for ticker, data in stock_data.items():
    print(f'{ticker}: EPS (TTM): {data["EPS (TTM)"]}, Previous Close: {data["Previous Close"]}, P/E Ratio: {data["P/E Ratio"]}')

