# Break camelCase
# https://www.codewars.com/kata/5208f99aee097e6552000148
# solution("camelCasing")  ==  "camel Casing"


def solution(s):
    result_string = ""
    for each_letter in s:
        if each_letter.isupper():
            result_string += f" {each_letter}"
        else:
            result_string += each_letter
    return result_string


def break_camel_case(string):
    return "".join(" " + letter if letter.isupper() else letter for letter in string)


print(solution("camelCasing"))
print(break_camel_case("camelCasing"))
