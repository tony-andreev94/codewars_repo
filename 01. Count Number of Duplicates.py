# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.


# my initial solution
def duplicates_func(text):
    text = text.lower()
    duplicates_list = []
    for char in set(text):
        counts = text.count(char)
        if counts > 1:
            duplicates_list.append(char)

    return len(duplicates_list)


# better alternative solution:
def duplicate_count(text):
    count = 0
    for char in set(text.lower()):
        if text.lower().count(char) > 1:
            count += 1
    return count


if __name__ == "__main__":
    input_string = input()
    # print(duplicate_count(input_string))
    print(duplicates_func(input_string))
