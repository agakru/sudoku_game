import random
from copy import copy

def board_to_sudoku():
    square=[]
    col=[]
    for g in range(9):
        square=[]
        for h in range(9):
            square.append(0)
        col.append(square)
    return(col)

def solution_sudoku(board):
    start_num=random.randint(1,9)
    variables=[0,6,3,2,8,5,7,4,1]
    for p in range(0,9):
        board[0][p]=start_num +variables[p]
        if board[0][p]>9:
            board[0][p]= board[0][p]-9
    z=1
    for g in range(0,9):
        for i in range(0,9):
            if g ==0:
                z-=1
                break
            board[g][i]=board[0][i]+z
            if board[g][i] >9:
                div=board[g][i]//9
                board[g][i]=board[g][i]-(div*9)
        z=z+1 
    # transform board to row and column sudoku 
    transform_sudoku=[]
    for row in range(0,9,3):
        for column in range(0,9,3):
            row_transform_sudoku=[]
            for j in range(0,3): 
                for i in range(0,3):
                    row_transform_sudoku.append(board[row+j][column+i])
            transform_sudoku.append(row_transform_sudoku)

    return(transform_sudoku)

def sudoku_with_empty(board):
    #min empty place 20 max 41 place in sudoku
    how_many_empty_place=random.randint(20,41)
    empty_place=0
    while how_many_empty_place!=empty_place:
        r_col=random.randint(0,8)
        r_row=random.randint(0,8)
        if  board[r_row][r_col]!=0:
            board[r_row][r_col]=0
            empty_place+=1
    
    #print('\n',board[0],'\n',board[1],'\n',board[2],'\n',board[3],'\n',board[4],'\n',board[5],'\n',board[6],'\n',board[7],'\n',board[8],'\n')
    return(board)

def possible(board,row,col,number):
    #is it the same number in the col ?
    for row_1 in range(9):
        if board[row_1][col]==number:
            return False
    #is it the same number in the row ?
    for col_1 in range(9):
        if board[row][col_1]==number:
            return False
    #is it the same number in the square ?
    num_row=(row//3)*3
    num_col=(col//3)*3
    for sq_r in range(num_row,num_row+3):
        for sq_c in range(num_col,num_col+3):
            if board[sq_r][sq_c]==number:
                return False
    return True

def find_empty_place(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
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
        if possible(board,row,col,number):
            board[row][col]=number
            if solve(board):
                return True
            else:
                board[row][col]=0
    return False                         

tab=board_to_sudoku()
sol_board=solution_sudoku(tab)
emp_board=sudoku_with_empty(sol_board)
solution=solve(emp_board)
print('\n',board_solved[0],'\n',board_solved[1],'\n',board_solved[2],'\n',board_solved[3],'\n',board_solved[4],'\n',board_solved[5],'\n',board_solved[6],'\n',board_solved[7],'\n',board_solved[8],'\n')