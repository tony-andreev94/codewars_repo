# Traffic Count During Peak Hours
# https://www.codewars.com/kata/586ed2dbaa0428f791000885
# 7 kyu

# a1 = [23,24,34,45,43,23,57,34,65,12,19,45, 54,65,54,43,89,48,42,55,22,69,23,93]
#
# traffic_count(a1) ==> [('4:00pm', 45), ('5:00pm', 65), ('6:00pm', 89), ('7:00pm', 93)]


def traffic_count(array):
    result_list = []
    for i in range(4, 8):
        result_list.append((f"{i}:00pm", max(array[:6])))
        del array[:6]

    return result_list


test_list = [23, 24, 34, 45, 43, 23, 57, 34, 65, 12, 19, 45, 54, 65, 54, 43, 89, 48, 42, 55, 22, 69, 23, 93]

print(traffic_count(test_list))

