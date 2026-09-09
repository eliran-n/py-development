
def max_profit(prices):

    buy_price = prices[0]
    buy_index = 0
    prices_len = len(prices)

    for i in range(1, prices_len):
        if prices[i] < buy_price:
            buy_price = prices[i]
            buy_index = i

    sell_price = buy_price
    for i in range(buy_index, prices_len):
        if prices[i] > sell_price:
            sell_price = prices[i]

    if sell_price <= buy_price:
        return 0
    else:
        return sell_price - buy_price


def max_profit_correct(prices):
    prices_len = len(prices)
    min_so_far = prices[0]
    max_profit_so_far = 0
    for i in range(1, prices_len):
        if prices[i] < min_so_far:
            min_so_far = prices[i]
        if (prices[i] - min_so_far) > max_profit_so_far:
            max_profit_so_far = (prices[i] - min_so_far)
    return max_profit_so_far

if __name__ == "__main__":

    prices_list = [7, 1, 5, 3, 6, 4]
    max_profit = max_profit(prices_list)
    print(max_profit)
