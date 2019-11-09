import requests

SESSION_ID = "k18axp5n9GM8sguSmqX7I4KYTQT5fLsP.m1-prod-api25"


def get_stocks_count():
    payload = {
        "start": 0,
        "end": 1,
        "country": "All",
        "orderType": "Asc",
        "sortType": "ByName"
    }
    resp = requests.post('https://api.tinkoff.ru/trading/stocks/list', json=payload)
    return resp.json()['payload']['total']


def enumerate_stocks(count=1):
    payload = {
        "start": 0,
        "end": count,
        "country": "All",
        "orderType": "Asc",
        "sortType": "ByName"
    }
    resp = requests.post('https://api.tinkoff.ru/trading/stocks/list', json=payload)
    stocks = resp.json()['payload']['values']

    results = list()

    for stock in stocks:

        price = stock['price'].get('value')
        currency = stock['price'].get('currency')
        name = stock['symbol'].get('showName')
        sector = stock['symbol'].get('sector')
        ticker = stock['symbol'].get('ticker')

        # exchange = stock['symbol']['exchange']
        # exchange_name = stock['symbol']['exchangeShowName']
        # county = stock['symbol']['countryOfRiskBriefName']

        results.append({
            'price': price,
            'currency': currency,
            'name': name,
            'sector': sector,
            'ticker': ticker,
        })

    return results


def get_fundamentals_for_ticker(ticker="ACN", sessionId=SESSION_ID):
    payload = {"ticker":ticker, "period":"year"}
    url = 'https://api.tinkoff.ru/trading/stocks/fundamentals'
    params = {'sessionId': sessionId}
    resp = requests.post(url, params=params, json=payload)

    pe = resp.json()['payload'].get('companyPE')
    market_cap = resp.json()['payload'].get('marketCap')
    if market_cap:
        market_cap = market_cap[0][1]
    dividend_yield = resp.json()['payload'].get('dividendYield')

    return {
        'pe': pe,
        'market_cap': market_cap,
        'dividend_yield': dividend_yield,
    }


def enrich_stocks_with_fundamentals(stocks, sessionId=SESSION_ID):
    for stock in stocks:
        fundamentals = get_fundamentals_for_ticker(ticker=stock['ticker'], sessionId=sessionId)
        stock.update(fundamentals)
    return stocks


def main():
    stocks_count = get_stocks_count()
    stocks = enumerate_stocks(count=stocks_count)
    stocks = enrich_stocks_with_fundamentals(stocks, sessionId=SESSION_ID)
    return stocks

    # s1 = list(filter(
    #     lambda s:(s['price'] < 40) and (s['currency'] == 'USD') and (s['dividend_yield'] and s['dividend_yield'] > 4),
    #     stocks
    # ))
    # s2 = sorted(s1, key=lambda s:s['market_cap'] or 0, reverse=True)
