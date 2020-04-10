# What dominates your array?
# https://www.codewars.com/kata/559e10e2e162b69f750000b4
# 7 kyu


def dominator(array):
    for each in array:
        if array.count(each) > len(array) / 2:
            return each
    return -1


def dominator_comprehension(array):
    result = "".join(set([str(each) for each in array if array.count(each) > len(array) / 2]))
    if not result == "":
        return result
    else:
        return -1


test_list = [13, 4, 12, 2, 3, 1, 11, 3]
print(dominator(test_list))
print(dominator_comprehension(test_list))
