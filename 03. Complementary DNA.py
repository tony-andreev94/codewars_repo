# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions"
# for the development and functioning of living organisms.#
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# You have function with one side of the DNA (string, except for Haskell);
# you need to get the other complementary side. DNA strand is never empty or there is no DNA at all.
# DNA_strand ("ATTGC") # return "TAACG"
# DNA_strand ("GTAT") # return "CATA"


def dna_test(dna):
    result_str = ''
    for each_char in dna:
        if each_char == 'A':
            result_str += 'T'
        elif each_char == 'T':
            result_str += 'A'
        elif each_char == 'C':
            result_str += 'G'
        elif each_char == 'G':
            result_str += 'C'

    return result_str


# alternative solution
def DNA_strand(dna):
    return ''.join([{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[letter] for letter in dna])


if __name__ == "__main__":
    dna_input = input()
    print(dna_test(dna_input))
    print(DNA_strand(dna_input))
