# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!
#
# Examples:
# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2


# initial solution
def get_sum(a, b):
    numbers_sum = 0
    if a <= b:
        for i in range(a, b + 1):
            numbers_sum += i
    else:
        for i in range(b, a + 1):
            numbers_sum += i

    return numbers_sum


# alternative solution
def get_sum_func(a, b):
    numbers_sum = 0
    for i in range(min(a, b), max(a, b) + 1):
        numbers_sum += i

    return numbers_sum


if __name__ == "__main__":
    first_num = int(input())
    second_num = int(input())
    print(get_sum(first_num, second_num))
