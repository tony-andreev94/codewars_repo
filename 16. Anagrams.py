# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false


def find_anagrams(word, list):
    temp_result = []
    result = []
    sorted_word = sorted(word)
    for each in list:
        if sorted(each) == sorted_word:
            result.append("".join(each))

    return result


def one_line_solution(word, list):
    return ["".join(each) for each in list if sorted(each) == sorted(word)]


word = input()
list_of_words = input().split(" ")
print(find_anagrams(word, list_of_words))
print(one_line_solution(word, list_of_words))
