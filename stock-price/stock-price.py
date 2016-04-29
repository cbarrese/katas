stock_prices = input('Enter stock prices:')

if len(stock_prices) < 2:
    raise IndexError('Need at least 2 stock prices')

buy_price = stock_prices[0]
sell_price = stock_prices[1]
min_price = min(buy_price, sell_price)
max_profit = sell_price - buy_price
for current_time, current_price in enumerate(stock_prices):

    if current_time <= 1:
        continue

    print current_time, current_price
    potential_profit = current_price - min_price

    if max_profit < potential_profit:
        sell_price = current_price
        buy_price = min_price
        max_profit = potential_profit

    min_price = min(min_price, current_price)

print "buy: %d sell: %d -> profit %d" % (buy_price, sell_price, max_profit)

