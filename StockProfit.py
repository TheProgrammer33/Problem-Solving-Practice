
"""
Given the daily values of a stock, create a function called max_profit_days() that,
given a list of integers, will return the index value of the two elements that represent
the day on which one should have bought a share and the day on which one should have sold a share based on the max profit.

A list of integers will represent the stock price at the beginning or “opening bell”
of each day for a week. You are required to buy and sell only once.
You also must buy a stock before selling it.

For example, given the list [7, 11, 60, 25, 150, 75, 31, 120],
you can assume that index 0 represents day 0 and index 7 represents day 7.
In this case, purchasing on day 1 and selling on day 4 would yield the most profit.
If we were to call max_profit_days([17, 11, 60, 25, 150, 75, 31, 120]), the function would return (1, 4).
"""

def max_profit_days(stock_prices):
    profit = stock_prices[1] - stock_prices[0] 
    profitPosition = (0, 1)
    for i in range(len(stock_prices)):
        startingPrice = stock_prices[i]
        for j in range(i+1, len(stock_prices)):
            priceDifference = stock_prices[j] - startingPrice
            if priceDifference > profit:
                profit = priceDifference
                profitPosition = (i, j)
                
    return profitPosition
