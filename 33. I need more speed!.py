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


def reverse(seq):
    result = list()
    for i in range(len(seq) - 1, -1, -1):
        result.append(seq[i])
    return result


my_list = [1, 2, 3, 4, 5]
print(reverse(my_list))
my_list2 = [{'b': 2}, {'a': 1}]
print(reverse(my_list2))
