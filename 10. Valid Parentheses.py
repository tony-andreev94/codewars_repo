# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true


def valid_parentheses(string):
    parentheses_counter = 0

    for each_char in string:
        if parentheses_counter < 0:
            break
        if each_char == "(":
            parentheses_counter += 1
        elif each_char == ")":
            parentheses_counter -= 1

    if parentheses_counter == 0:
        return True
    else:
        return False


input_string = input()
print(valid_parentheses(input_string))
