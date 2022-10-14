from tkinter import *
from Solver import solver
root = Tk()
root.title("Sudoku Solver")
root.geometry("324x550") # 320 pixels by width 550 pixels by height

label = Label(root, text='Fill in the numbers and click solve')
label.grid(row = 0, column = 1, columnspan = 10)

solvedLabel = Label(root, text="", fg='green')
solvedLabel.grid(row = 11, column = 1, columnspan = 10)

cells = {}

def ValidateNumber(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out

reg = root.register(ValidateNumber)

def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify='center', validate="key", validatecommand=(reg, '%P'))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = e

def draw9x9Grid():
    color = "#CBC3E3"
    for rowNo in range(1,10, 3):
        for ColumnNo in range(0, 9, 3):
            draw3x3Grid(rowNo, ColumnNo, color)
            if color == '#CBC3E3':
                color = "#ffffff"
            else:
                color = "#CBC3E3"

def clearValues():
    solvedLabel.configure(text='')
    for row in range(2, 11):
        for column in range(1,10):
            # get the entry widget from the cells dictionary at the given row and column and clear it
            cell = cells[(row, column)]
            cell.delete(0, "end")

def getValues():
    board = []
    solvedLabel.configure(text="")
    # get the values from the cells and store them in a list, call the updateValues function
    for row in range(2, 11):
        rowList = []
        for column in range(1,10):
            cell = cells[(row, column)]
            if cell.get() == '':
                rowList.append(0)
            else:
                rowList.append(int(cell.get()))
        board.append(rowList)
    updateValues(board)



btn = Button(root, command=getValues, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

btn = Button(root, command=clearValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)

def updateValues(s):
    #call the solver function and get the solved board
    solvedBoard = solver(s)
    #if the board is not solved
    if solvedBoard != False:
        #update the cells with the solved board
        for row in range(2, 11):
            for column in range(1,10):
                cell = cells[(row, column)]
                cell.delete(0, "end")
                cell.insert(0, solvedBoard[row-2][column-1])
        solvedLabel.configure(text="Sudoku Solved!", fg='green')
    else:
        # when it prints i get a blank line in the error label
        solvedLabel.configure(text="No Solution", fg='red')



draw9x9Grid()
root.mainloop()


