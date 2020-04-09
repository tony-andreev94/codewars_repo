# Build Tower
# https://www.codewars.com/kata/576757b1df89ecf5bd00073b

# test.assert_equals(tower_builder(2), [' * ', '***'])
# test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])


def tower_builder(n_floors):
    tower_list = []
    star_count = 1
    space_count = 0
    new_list = []
    # build tower floors and stars
    for i in range(1, n_floors + 1):
        tower_list.append('*' * star_count)
        star_count += 2

    # add whitespace to lower floors
    for each in reversed(tower_list):
        each = " " * space_count + each + " " * space_count
        new_list.append(each)
        space_count += 1

    return new_list[::-1]


print(tower_builder(5))
