# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Example with 3 floors:
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]


def tower_builder(n_floors):
    star_counter = 1
    floor_counter = 0
    whitespace_counter = n_floors - 1
    result_string = "[\n"

    while floor_counter < n_floors:
        result_string += "  '"
        result_string += " " * whitespace_counter
        result_string += "*" * star_counter
        result_string += " " * whitespace_counter
        result_string += "',\n"

        whitespace_counter -= 1
        star_counter += 2
        floor_counter += 1

    result_string += "]"

    return result_string


floors = int(input())
print(tower_builder(floors))
