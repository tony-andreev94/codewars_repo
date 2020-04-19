# https://www.codewars.com/kata/55de9c184bb732a87f000055
# 6 kyu
"""
Remove this comment otherwise your code cannot pass the anti-cheat tests!

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use "x=list()" instead if you need it
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.
"""


# not accepted by codewars
def reverse(seq):
    result = list()
    for i in range(len(seq) - 1, -1, -1):
        result.append(seq[i])
    seq = result
    return seq


# performance ineffective - time out
def reverse2(seq):
    up_bound = len(seq)
    index = len(seq) - 1
    while index >= 0:
        seq.append(seq[index])
        index -= 1

    for i in range(up_bound):
        seq.pop(0)
    return seq


# performance ineffective, exec time x2.3
def reverse3(seq):
    for i in range(-1, -(len(seq) + 1), -1):
        seq.append(seq[i])
        if i == -len(seq):
            seq.pop(0)
        else:
            seq.pop(i - 1)
    return seq


def reverse4(seq):
    length = len(seq)
    counter = -1
    while True:
        if abs(counter) == length:
            seq.append(seq[counter])
            seq.pop(0)
            break

        seq.append(seq[counter])
        counter -= 1
        seq.pop(counter)
    return seq


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
#            30, 31, 32, 33, 34, 35, 36, 37, 38, 10, 39, 40]
my_list = [1, 2, 3, 4, 5]
print(reverse(my_list))
my_list2 = [{'b': 2}, {'a': 1}]
print(reverse4(my_list2))
