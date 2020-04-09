# Snail Sort
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python


def snail(snail_map):
    result_list = []
    if len(snail_map[0]) > 0:
        while len(snail_map) > 0:

            # go right
            while len(snail_map[0]) > 0:
                result_list.append((snail_map[0])[0])
                snail_map[0].pop(0)
                if len(snail_map[0]) == 0:
                    snail_map.pop(0)
                    break
            if len(snail_map) == 0:
                break

            # go down
            for counter in range(len(snail_map)):
                result_list.append((snail_map[counter])[-1])
                snail_map[counter].pop(-1)

            # go left
            for each in reversed(snail_map[-1]):
                result_list.append(each)
                (snail_map[-1]).pop(-1)
                if len(snail_map[-1]) == 0:
                    snail_map.pop(-1)
                    break
            if len(snail_map) == 0:
                break

            # go up
            for up_count in reversed(range(len(snail_map))):
                result_list.append((snail_map[up_count])[0])
                snail_map[up_count].pop(0)
            if len(snail_map) == 0:
                break

        return result_list
    else:
        return []


# Testing:
array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

list_t = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

empty = [[]]

print(snail(array))
print(snail(list_t))
print(snail(empty))
