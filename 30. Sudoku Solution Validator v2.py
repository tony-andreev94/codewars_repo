# Sudoku Solution Validator
# https://www.codewars.com/kata/529bf0e9bdf7657179000008
# 4 kyu


def validate_sudoku(board):
    if validate_rows(board) and validate_columns(board) and validate_quadrants(board):
        return True
    else:
        return False


def validate_rows(board):
    valid_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for each_row in board:
        if not sorted(each_row) == valid_list:
            return False
    return True


def validate_columns(board):
    valid_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    temp_list = []
    for i in range(9):
        for each in board:
            temp_list.append(each[i])
        if not sorted(temp_list) == valid_list:
            return False
        temp_list = []
    return True


def validate_quadrants(board):
    valid_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quadrant_one = []
    quadrant_two = []
    quadrant_three = []
    for i in range(9):
        for each in board:
            if len(quadrant_one) < 9:
                quadrant_one.extend(each[:3])
                quadrant_two.extend(each[3:6])
                quadrant_three.extend(each[-3:])

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
    return True


board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 0, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]
         ]

print(validate_sudoku(board))