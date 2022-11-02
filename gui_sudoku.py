import pygame
import sys
from sudokugame import *
import time
from copy import deepcopy

WIDHT_SCREEN=550
HEIGHT_SCREEN=600
BLUE=(0, 0, 255)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
GREY=(150, 150, 150)
WIDTH_LINE=2
SIZE_FONT=32
HEIGHT_BUTTON=25
WIDHT_BUTTON=100
GAP=50
MAX_SEC=60

board=creat_board_to_sudoku()
solved_board=solution_sudoku(board)
board_to_solve=creat_sudoku_with_empty_place(solved_board)
trial_board_to_solve=deepcopy(board_to_solve)
temp_board=[ 
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

if solve(trial_board_to_solve):
    run=True

pygame.init()
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()

screen = pygame.display.set_mode([WIDHT_SCREEN, HEIGHT_SCREEN])
base_font = pygame.font.Font(None, SIZE_FONT)

active=False

key= ' '
mistake = 0
rectangle = [0,0]
pos_x, pos_y= 0,0
start = time.time()
anwser= ' '
button_restart=pygame.Rect(50,520,WIDHT_BUTTON,HEIGHT_BUTTON)
button_quit=pygame.Rect(400,520,WIDHT_BUTTON,HEIGHT_BUTTON)
button_solve=pygame.Rect(170,520,WIDHT_BUTTON,HEIGHT_BUTTON)
button_hint=pygame.Rect(290,520,WIDHT_BUTTON,HEIGHT_BUTTON)

def place_clicked(pos_x, pos_y):
    if pos_x > 50 and pos_x < 500 and pos_y > 50 and pos_y < 500:
        col_x=pos_x // GAP
        row_y=pos_y // GAP
        for row in range(1, 10):
            for col in range(1, 10):
                if col_x == col and row_y == row:
                    if board_to_solve[row - 1][col - 1] == 0:
                            return True
    else:
        return False

def restart_clicked(pos_x, pos_y):
    if pos_x > 50 and pos_x < 150 and pos_y > 520 and pos_y < 545:
        return True
    else:
        return False

def quit_clicked(pos_x, pos_y):
    if pos_x > 400 and pos_x < 500 and pos_y > 520 and pos_y < 545:
        return True
    else:
        return False
def hint_clicked(pos_x, pos_y):
    if pos_x > 290 and pos_x < 390 and pos_y > 520 and pos_y < 545:
        return True
    else:
        return False  

def hint(previous_pos_x, previous_pos_y, temp_board):
    col_x =(previous_pos_x // GAP) - 1
    row_y=(previous_pos_y //GAP) - 1 
    temp_board[row_y][col_x]=trial_board_to_solve[row_y][col_x]
    return temp_board

def solve_clicked(pos_x, pos_y):
    if pos_x > 170 and pos_x < 270 and pos_y > 520 and pos_y < 545:
        return True
    else:
        return False

def solve_place():
    temp_board=trial_board_to_solve
    return temp_board
        
def checked(pos_x, pos_y, key):
    col_x=pos_x // GAP
    row_y=pos_y // GAP
    for row in range(1, 10):
        for col in range(1, 10):
            if col_x == col and row_y == row:
                temp_board[row - 1][col - 1] = key         
    return temp_board

def clear_board(new_temp_board):
    new_temp_board=[ 
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    return new_temp_board

def check_if_solved(board):
    result=[ 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    for row in range(NUMBER_OF_CELL):
        for col in range(NUMBER_OF_CELL):
            result[row][col]=board[row][col] + board_to_solve[row][col] 
    if result == trial_board_to_solve:
        return True
    else:
        return False

def check_mistakes(pos_x, pos_y, board):
    col_x=(pos_x // GAP) - 1
    row_y=(pos_y // GAP) - 1
    if board_to_solve[row_y][col_x] == 0:
        if board[row_y][col_x] != trial_board_to_solve[row_y][col_x]:
            return False
    return True       

def format_time(time_in_sec):
    sec = time_in_sec % MAX_SEC
    minute = time_in_sec // MAX_SEC
    hour = minute // MAX_SEC
    time_str = str(hour) + ":" + str(minute) + ":" + str(sec)
    struct_time=time.strptime(time_str, "%H:%M:%S")
    time_format=time.strftime("%H:%M:%S", struct_time)
    return time_format

while run:
    
    screen.fill(WHITE)
    play_time = round(time.time() - start)
    
    btn_restart=pygame.draw.rect(screen, GREY, button_restart)
    text_surf =base_font.render("Restart", True, BLACK)
    screen.blit(text_surf, (button_restart.x+10, button_restart.y))

    btn_quit=pygame.draw.rect(screen, GREY, button_quit)
    text_surf =base_font.render("Quit", True, BLACK)
    screen.blit(text_surf, (button_quit.x+25, button_quit.y))

    btn_solve=pygame.draw.rect(screen, GREY, button_solve)
    text_surf =base_font.render("Solve", True, BLACK)
    screen.blit(text_surf, (button_solve.x+20, button_solve.y))

    btn_hint=pygame.draw.rect(screen, GREY, button_hint)
    text_surf =base_font.render("Hint", True, BLACK)
    screen.blit(text_surf, (button_hint.x+25, button_hint.y))

    for cell in range(10):
        if cell % 3 == 0:
            pygame.draw.line(screen, BLACK, (GAP + GAP * cell, GAP), (GAP + GAP * cell, 500), 5)
            pygame.draw.line(screen, BLACK, (GAP ,GAP + GAP * cell), (500 ,GAP + GAP * cell), 5)
        else:   
            pygame.draw.line(screen, BLACK, (GAP + GAP * cell, GAP), (GAP + GAP * cell, 500), WIDTH_LINE)
            pygame.draw.line(screen, BLACK, (GAP, GAP + GAP * cell), (500, GAP + GAP * cell), WIDTH_LINE)
    for row in range(NUMBER_OF_CELL):
        for col in range(NUMBER_OF_CELL):
            if board_to_solve[row][col] != 0:
                constant_numbers=base_font.render(str(board_to_solve[row][col]), True, BLUE)
                place_x_to_write=((col + 1) * GAP + 20)
                place_y_to_write=((row + 1) * GAP + 15) 
                screen.blit(constant_numbers, (place_x_to_write, place_y_to_write))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_BACKSPACE:
                    key = 0
                if event.key == pygame.K_RETURN:
                    if check_mistakes(pos_x, pos_y, temp_board):
                        anwser='Success'
                        active=False
                    else:
                        mistake+=1
                        anwser='Wrong'
                        active=False

                    if check_if_solved(temp_board):
                        value_end=base_font.render(f"Congratulation! You made {mistake} mistakes", True, BLACK)
                        screen.blit(value_end, (30, 545))

                    active=False

                if event.key == pygame.K_DELETE:
                    temp_board=clear_board(temp_board)
                    key = 0     

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            if place_clicked(pos_x, pos_y):
                if temp_board[pos_y // GAP - 1][pos_x // GAP - 1] != 0:
                    key=temp_board[pos_y // GAP - 1][pos_x // GAP - 1]
                else:
                    key=0
                active=True
                previous_pos_x, previous_pos_y=pos_x, pos_y    
            elif restart_clicked(pos_x, pos_y):
                active=False
                temp_board=clear_board(temp_board)
                mistake=0
                key=0  
                start=time.time()
            elif quit_clicked(pos_x, pos_y):
                pygame.quit()
                sys.exit()
            elif solve_clicked(pos_x, pos_y):
                active=False
                temp_board=solve_place()
            elif hint_clicked(pos_x, pos_y):
                active=False
                if place_clicked(previous_pos_x, previous_pos_y):
                    temp_board=hint(previous_pos_x, previous_pos_y, temp_board)
                    
            else:
                active=False

    if active:
        rectangle=pygame.draw.rect(screen, GREY, (((pos_x // GAP) * GAP) + WIDTH_LINE, ((pos_y // GAP) * GAP) + WIDTH_LINE, GAP - WIDTH_LINE, GAP - WIDTH_LINE))
        temp_board=checked(pos_x, pos_y, key)    
    else:
        key=' '   

    for row in range(NUMBER_OF_CELL):
        for col in range(NUMBER_OF_CELL):
            if temp_board[row][col] != 0:
                input_numbers=base_font.render(str(temp_board[row][col]), True, BLACK)
                place_x_to_write=((col + 1) * GAP +  20)
                place_y_to_write=((row + 1) * GAP + 15) 
                screen.blit(input_numbers, (place_x_to_write, place_y_to_write))
    
    value_mistake=base_font.render(anwser, True, BLACK)
    screen.blit(value_mistake, (50, 20)) 

    if check_if_solved(temp_board):
        value_end=base_font.render(f"Congratulation! You made {mistake} mistakes", True, BLACK)
        screen.blit(value_end,(30, 545))

    time_str=base_font.render("Time:" + format_time(play_time), 1, BLACK)
    screen.blit(time_str, (350, 20))  

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

