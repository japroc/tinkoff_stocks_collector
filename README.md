# tinkoff_stocks_collector
Collects info about available stocks at Tinkoff.Invest

# How To Use
1. Залогиниться на https://www.tinkoff.ru/invest/.
2. Get cookie `psid`. Значение выглядит примерно так: `jqqp8akVZMzsaER83vR5jDc3y9g5NHtt.m1-prod-api46`.
3. Заменить значение переменной `SESSION_ID` в начале скрипта на значение куки `psid`.
4. Получить список акций. Из консоли. Удобно через IPython:
```
stocks = main()
```
5. Фильтруем и сортируем. Например: цена < 50, только USD, дивидендная доходность больше 4 (но в Тинькове она странно считается). Сортировка по капитализации.
```
s1 = list(filter(
    lambda s:(s['price'] < 50) and (s['currency'] == 'USD') and (s['dividend_yield'] and s['dividend_yield'] > 4),
    stocks
))
s2 = sorted(s1, key=lambda s:s['market_cap'] or 0, reverse=True)
```
6. 
```
In [95]: s2[:3]
Out[95]:
[{'price': 39.5,
  'currency': 'USD',
  'name': 'AT&T',
  'sector': 'Telecom',
  'ticker': 'T',
  'pe': 18.4594,
  'market_cap': 287670900000,
  'dividend_yield': 5.18029},
 {'price': 37.1,
  'currency': 'USD',
  'name': 'British American Tobacco',
  'sector': 'Consumer',
  'ticker': 'BTI',
  'pe': 11.06801,
  'market_cap': 84807580000,
  'dividend_yield': 7.08117},
 {'price': 11.77,
  'currency': 'USD',
  'name': 'Vale SA',
  'sector': 'Materials',
  'ticker': 'VALE',
  'pe': 17.75694,
  'market_cap': 62424150000,
  'dividend_yield': 4.13793}]
```
