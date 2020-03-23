# In this kata you have to create all permutations of an input string and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.


def permutations(string, step=0):
    if step == len(string):
        print("".join(string))
    for i in range(step, len(string)):
        string_copy = [character for character in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permutations(string_copy, step + 1)


word = input()
print(permutations(word))
