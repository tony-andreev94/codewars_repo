# https://www.codewars.com/kata/58f174ed7e9b1f32b40000ec
# 6 kyu


# performance not considered
def max_profit(prices):
    profits_list = []

    for buy in prices:
        index = prices.index(buy)
        if index == len(prices) - 1:
            profits_list.append(0 - buy)
            return max(profits_list)
        for sell in prices[index + 1:]:
            profit = sell - buy
            profits_list.append(profit)
    return max(profits_list)


# performance considered
def max_profit2(prices):
    max_profit = prices[1] - prices[0]
    min_buy = prices[0]
    for i in range(1, len(prices)):
        profit = prices[i] - min_buy
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_buy:
            min_buy = prices[i]
    return max_profit


my_list = [10, 7, 5, 8, 11, 9]
print(max_profit2(my_list))
