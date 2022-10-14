N = 9
count = 0


def isSafe(sudoku, row, column, num):
    """Check if num can be placed in the given row, column"""
    # check if we find the same num in the similar row , we return False
    for x in range(9):
        if sudoku[row][x] == num:
            return False

    # check if we find the same num in the similar column , we return False
    for x in range(9):
        if sudoku[x][column] == num:
            return False

    # check if we find the same num in the particular 3*3 matrix, we return False
    startRow = row - row % 3
    startCol = column - column % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + startRow][j + startCol] == num:
                return False
    return True


def solveSudoku(sudoku, row, column):
    global count
    count += 1

    if count > 1000000:
        return False

    if row == N - 1 and column == N:
        return True

    if column == N:
        row += 1
        column = 0

    if sudoku[row][column] > 0:
        return solveSudoku(sudoku, row, column + 1)

    for num in range(1, N + 1, 1):
        if isSafe(sudoku, row, column, num):
            sudoku[row][column] = num
            if solveSudoku(sudoku, row, column + 1):
                return True
        sudoku[row][column] = 0
    return False


def solver(sudoku):
    global count
    # if solveSudoku returns True, the sudoku is solved
    if solveSudoku(sudoku, 0, 0):
        count = 0
        return sudoku
    else:
        count = 0
        return False
