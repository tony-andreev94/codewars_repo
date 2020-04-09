# Rot13
# https://www.codewars.com/kata/530e15517bc88ac656000716
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it.
# If there are numbers or special characters included in the string, they should be returned as they are.


def rot13(message):
    encrypted = ""
    for each in message:
        if each.isalpha():
            each_ord = ord(each)
            each_ord += 13
            if each.islower() and each_ord > 122 or each.isupper() and each_ord > 90:
                each_ord -= 26
            encrypted += chr(each_ord)
        else:
            encrypted += each
    return encrypted


print(rot13('test'))
print(rot13('TEST'))

