# Replacement
# https://www.codewars.com/kata/598d89971928a085c000001a

# Choose exactly one element from the sequence and replace it with another integer > 0.
# You are not allowed to replace a number with itself, or to change no number at all.
# Find the lowest possible sequence after performing a valid replacement, and sorting the sequence.

# ([1,2,3,4,5])  =>  [1,1,2,3,4]
# ([4,2,1,3,5])  =>  [1,1,2,3,4]
# ([2,3,4,5,6])  =>  [1,2,3,4,5]
# ([2,2,2])      =>  [1,2,2]
# ([1,1,1])      =>  [1,1,2]
# ([42])         =>  [1]


def sort_number(a):
    if max(a) == 1:
        a.remove(max(a))
        a.append(2)
    else:
        a.remove(max(a))
        a.append(1)

    sorted_result = sorted(a)

    return sorted_result


if __name__ == '__main__':
    a = [4, 2, 1, 3, 5]
    print(sort_number(a))

