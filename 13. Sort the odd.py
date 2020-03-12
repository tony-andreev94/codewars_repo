# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.
# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example:
# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


def sort_array(source_array):
    odd_array = []
    for each_item in source_array:
        if not each_item % 2 == 0:
            odd_array.append(each_item)

    odd_array.sort()

    index = 0
    counter = 0
    for each_el in source_array:
        if not each_el % 2 == 0:
            source_array[index] = odd_array[counter]
            counter += 1
        index += 1

    return source_array
