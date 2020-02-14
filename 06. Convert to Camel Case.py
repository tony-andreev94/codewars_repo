# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples:
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"


# my initial solution
def to_camel_case(text):
    if '-' in text or '_' in text:  # exception handling if text has no '-' or '_'
        while '-' in text or '_' in text:
            for each_char in text:
                if each_char == '_' or each_char == '-':
                    index = text.index(each_char)
                    new_text = text[:index] + text[index + 1].upper() + text[index + 2:]
            text = new_text

        return new_text
    else:
        return text


# better alternative solution with .title()
# The title() method returns a copy of the string in which first characters of all the words are capitalized.
def to_camel_case_func(text):
    new_text = text[:1] + text.title().replace('-', "").replace('_', "")[1:]
    return new_text


if __name__ == "__main__":
    input_string = input()
    print(to_camel_case_func(input_string))
