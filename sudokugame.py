import random 
from copy import copy
NUMBER_OF_CELL = 9

def creat_board_to_sudoku(): 
    col=[]
    for row in range(NUMBER_OF_CELL):
        square=[]
        for column in range(NUMBER_OF_CELL):
            square.append(0)
        col.append(square)
    return(col)

def solution_sudoku(board):
    start_number=random.randint(1, 9)
    difference_beetween_cells=[0, 6, 3, 2, 8, 5, 7, 4, 1]
    for place in range(NUMBER_OF_CELL):
        board[0][place]=start_number + difference_beetween_cells[place]
        if board[0][place] > NUMBER_OF_CELL:
            board[0][place]= board[0][place] - NUMBER_OF_CELL
    difference_beetwen_squares=1
    for row in range(NUMBER_OF_CELL):
        for col in range(NUMBER_OF_CELL):
            if row == 0:
                difference_beetwen_squares -= 1 
                break
            board[row][col]=board[0][col]+difference_beetwen_squares
            if board[row][col] > NUMBER_OF_CELL:
                divided=board[row][col] // NUMBER_OF_CELL
                board[row][col]=board[row][col]-(divided * NUMBER_OF_CELL)
        difference_beetwen_squares=difference_beetwen_squares+1 
        
    transform_sudoku=[]
    for row in range(0, NUMBER_OF_CELL, 3):
        for column in range(0, NUMBER_OF_CELL, 3):
            row_transform_sudoku=[]
            for row_in_square in range(0, 3): 
                for col_in_square in range(0, 3):
                    row_transform_sudoku.append(board[row+row_in_square][column+col_in_square])
            transform_sudoku.append(row_transform_sudoku)

    return(transform_sudoku)

def creat_sudoku_with_empty_place(board):
    empty_places_number=random.randint(20, 41)
    empty_place_counter=0
    while empty_places_number != empty_place_counter:
        r_col=random.randint(0, NUMBER_OF_CELL-1)
        r_row=random.randint(0, NUMBER_OF_CELL-1)
        if  board[r_row][r_col] != 0:
            board[r_row][r_col] = 0
            empty_place_counter += 1
    
    #print('\n',board[0],'\n',board[1],'\n',board[2],'\n',board[3],'\n',board[4],'\n',board[5],'\n',board[6],'\n',board[7],'\n',board[8],'\n')
    return(board)

def check_if_number_is_possible(board, row, col, number): 
    #is it the same number in the col ?
    for row_1 in range(NUMBER_OF_CELL):
        if board[row_1][col] == number:
            return False
    #is it the same number in the row ?
    for col_1 in range(NUMBER_OF_CELL):
        if board[row][col_1] == number:
            return False
    #is it the same number in the square ?
    number_row=(row // 3) * 3
    nummber_col=(col // 3) * 3
    for sq_r in range(number_row, number_row + 3):
        for sq_c in range(nummber_col,nummber_col + 3):
            if board[sq_r][sq_c] == number:
                return False
    return True

def find_empty_place(board):
    for row in range(NUMBER_OF_CELL):
        for col in range(NUMBER_OF_CELL):
            if board[row][col] == 0:
                return(row,col)
    return                  

board_solved=[[]]
def solve(board):
    global board_solved
    find=find_empty_place(board)
    if find is None:
        board_solved=copy(board)
        return True
    else:
        row, col = find

    for number in range(1,10):
        if check_if_number_is_possible(board, row, col, number):
            board[row][col]=number
            if solve(board):
                return True
            else:
                board[row][col] = 0
    return False                         

tab=creat_board_to_sudoku()
sol_board=solution_sudoku(tab)
emp_board=creat_sudoku_with_empty_place(sol_board)
solution=solve(emp_board)
print('\n', board_solved[0], '\n', board_solved[1], '\n', board_solved[2], '\n', board_solved[3], '\n', board_solved[4], '\n', board_solved[5], '\n', board_solved[6], '\n', board_solved[7], '\n', board_solved[8], '\n')