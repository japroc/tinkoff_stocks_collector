# tinkoff_stocks_collector
Collects info about available stocks at Tinkoff.Invest

# How To Use
1. Залогиниться на https://www.tinkoff.ru/invest/.
2. Get cookie `psid`. Значение выглядит примерно так: `jqqp8akVZMzsaER83vR5jDc3y9g5NHtt.m1-prod-api46`.
3. Заменить значение переменной `SESSION_ID` в начале скрипта на значение куки `psid`.
4. Получить список акций. Из консоли:
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
