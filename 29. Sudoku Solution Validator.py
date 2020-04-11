# Sudoku Solution Validator
# https://www.codewars.com/kata/529bf0e9bdf7657179000008
# 4 kyu


def valid_solution(board):
    column_list = []
    quadrant_one = []
    quadrant_two = []
    quadrant_three = []
    valid_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        for each in board:
            # check row
            if not sorted(each) == valid_list:
                return False
            # build column
            column_list.append(each[i])
            # build quadrants
            if len(quadrant_one) < 9:
                quadrant_one.extend(each[:3])
                quadrant_two.extend(each[3:6])
                quadrant_three.extend(each[-3:])

        # check column
        if not sorted(column_list) == valid_list:
            return False
        # check quadrants
        if i == 2 or i == 5 or i == 8:
            if not sorted(quadrant_one) == valid_list:
                return False
            quadrant_one = []

            if not sorted(quadrant_two) == valid_list:
                return False
            quadrant_two = []

            if not sorted(quadrant_three) == valid_list:
                return False
            quadrant_three = []

        column_list = []

    return True


board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

print(valid_solution(board))
