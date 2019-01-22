from test_framework import generic_test

# 5.6
def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    mi = prices[0]
    ma = 0
    for p in prices:
        ma = max(ma, p - mi)
        mi = min(mi, p)
    return ma


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
