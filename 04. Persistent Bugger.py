# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.
# Examples:
#  persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.
#
#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.
#
#  persistence(4) => 0   # Because 4 is already a one-digit number.
from functools import reduce


# my initial solution
def persistence(number):
    # your code
    iterations = 0
    while number > 9:
        digit_sum = 1
        for each_digit in str(number):
            digit_sum *= int(each_digit)
        number = digit_sum
        iterations += 1

    return iterations


# alternative better solution
def persistence_func(n, result=0):
    if len(str(n)) == 1:
        return result
    else:
        return persistence_func(reduce(lambda x, y: int(x) * int(y), str(n), 1), result + 1)


if __name__ == "__main__":
    num = int(input())
    print(persistence(num))
