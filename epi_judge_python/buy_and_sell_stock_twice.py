from test_framework import generic_test

# # 5. - O(n^2)
# def buy_and_sell_stock_twice(prices):
#     # TODO - you fill in here.

#     ma = 0
#     for i in range(len(prices)):
#         ma = max(ma, exchange(prices[:i]) + exchange(prices[i:]))
#     return ma

# def exchange(prices):
#     ma = 0
#     if not len(prices): return ma
    
#     mi = prices[0]
#     for p in prices:
#         ma = max(ma, p - mi)
#         mi = min(mi, p)
#     return ma

# 5. - O(n): use forward and backward
def buy_and_sell_stock_twice(prices):
    # TODO - you fill in here.
    ma = 0
    mi = float('inf')
    profits = [0] * len(prices)
    # forward
    for i, p in enumerate(prices):
        mi = min(mi, p)
        ma = max(ma, p = mi)
        profits[i] = ma
    
    # backward: make the second buy on day i
    ma = 0
    for i, p in enumerate(prices):
        pass # todo

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
