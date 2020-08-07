# Buy and sell a stock once
sequence_of_stock_prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


# Write a program that takes an array denoting the daily stock price
# returns max profit that could be made, don't sell if not profit is made

def max_profit(prices):
    min_price, max_price = 1000000, 0
    for price in prices:
        max_profit_today = price - min_price
        max_profit = max(max_profit_today, max_price)
        min_price = min(price, min_price)

    return max_profit
