# Find Screen Size
# https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f
# 7 kyu

# test.assert_equals(find_screen_height(1024, "4:3"), "1024x768")
# test.assert_equals(find_screen_height(1280, "16:9"), "1280x720")


def find_screen_height(width, ratio):
    first_ratio = int(ratio[:(ratio.index(':'))])
    second_ratio = int(ratio[(ratio.index(':')) + 1:])
    height = int(width / first_ratio * second_ratio)
    return f"{width}x{height}"


def find_screen_height_comprehension(width, ratio):
    return f"{width}x{int(width / int(ratio[:(ratio.index(':'))]) * int(ratio[(ratio.index(':')) + 1:]))}"


print(find_screen_height(1024, "4:3"))
print(find_screen_height_comprehension(1024, "4:3"))
