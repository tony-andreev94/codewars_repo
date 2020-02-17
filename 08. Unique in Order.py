# Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.
#
# Examples:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


# initial solution
def unique_in_order(iterable):
    iterable_str = ''
    result_list = []
    previous_char = 128
    # loop to handle int arrays
    for each_digit in iterable:
        if 48 <= ord(str(each_digit)) <= 57:
            iterable_str += str(each_digit)

    if not len(iterable_str) == 0:
        iterable = iterable_str

    for each_char in iterable:
        if ord(each_char) != previous_char:
            if 48 <= ord(each_char) <= 57:
                result_list.append(int(each_char))
            else:
                result_list.append(each_char)
        previous_char = ord(each_char)

    return result_list


if __name__ == "__main__":
    input_string = input()
    print(unique_in_order(input_string))
