# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
#
# Example:
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)


# initial solution
def alphabet_position(text):
    result_str = ''
    new_text = text.lower()
    for each_char in new_text:
        if 97 <= ord(each_char) <= 122:
            result_str += str(ord(each_char) - 96) + ' '

    return result_str.rstrip()


# alternative solution
def alpha_position(text_input):
    result_str = ''
    for each_char in text_input:
        if each_char.isalpha():
            result_str += str(ord(each_char.lower()) - 96) + ' '

    return result_str.rstrip()


if __name__ == "__main__":
    string_input = input()
    print(alpha_position(string_input))
