import pygame
import sys
from sudokugame import *
import time
from copy import deepcopy

board=board_to_sudoku()
solved_board=solution_sudoku(board)
board_to_solve=sudoku_with_empty(solved_board)
check_if_board_can_solve=deepcopy(board_to_solve)
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

if solve(check_if_board_can_solve):
    run=True

pygame.init()
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()
  
screen = pygame.display.set_mode([550, 600])
base_font = pygame.font.Font(None, 32)
color_of_numbers=(0,0,255)
width_line=2
active=False

global pos
global rectangle
global mistake
global key
global previous_pos
key=' '
mistake=0
rectangle=[0,0]
pos= 0,0
start = time.time()
anwser=' '
button_restart=pygame.Rect(50,520,100,25)
button_quit=pygame.Rect(400,520,100,25)
button_solve=pygame.Rect(170,520,100,25)
button_hint=pygame.Rect(290,520,100,25)

def place_clicked(pos):
    if pos[0]>50 and pos[0]<500 and pos[1]>50 and pos[1]<500:
        gap=50
        x =pos[0]//gap
        y=pos[1]//gap
        for i in range(1,10):
            for j in range(1,10):
                if x==j and y==i:
                    if board_to_solve[i-1][j-1]==0:
                            return True
    else:
        return False

def restart_clicked(pos):
    if pos[0]>50 and pos[0]<150 and pos[1]>520 and pos[1]<545:
        return True
    else:
        return False

def quit_clicked(pos):
    if pos[0]>400 and pos[0]<500 and pos[1]>520 and pos[1]<545:
        return True
    else:
        return False
def hint_clicked(pos):
    if pos[0]>290 and pos[0]<390 and pos[1]>520 and pos[1]<545:
        return True
    else:
        return False  

def hint(pre_pos,temp_board):
    gap=50
    y =(pre_pos[0]//gap)-1
    x=(pre_pos[1]//gap)-1
    temp_board[x][y]=check_if_board_can_solve[x][y]
    return temp_board

def solve_clicked(pos):
    if pos[0]>170 and pos[0]<270 and pos[1]>520 and pos[1]<545:
        return True
    else:
        return False

def solve_place(pos):
    temp_board=check_if_board_can_solve
    return temp_board
        
def checked(key):
    gap=50
    x =pos[0]//gap
    y=pos[1]//gap
    for i in range(1,10):
        for j in range(1,10):
            if x==j and y==i:
                temp_board[i-1][j-1]=key         
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
    for i in range(9):
        for j in range(9):
            result[i][j]=board[i][j]+board_to_solve[i][j] 
    if result==check_if_board_can_solve:
        return True
    else:
        return False

def check_mistakes(pos,board):
    gap=50
    y =(pos[0]//gap)-1
    x=(pos[1]//gap)-1
    if board_to_solve[x][y]==0:
        if board[x][y]!=check_if_board_can_solve[x][y]:
            return False
    return True       

def format_time(time_in_sec):
    sec = time_in_sec%60
    minute = time_in_sec//60
    hour = minute//60
    time_str = str(hour) + ":"+ str(minute) + ":" + str(sec)
    struct_time=time.strptime( time_str,"%H:%M:%S")
    time_format=time.strftime("%H:%M:%S",struct_time)
    return time_format

while run:
    
    screen.fill((255, 255, 255))
    play_time = round(time.time() - start)
    
    btn_restart=pygame.draw.rect(screen,(150,150,150),button_restart)
    text_surf =base_font.render("Restart", True, (0,0,0))
    screen.blit(text_surf, (button_restart.x+10,button_restart.y))

    btn_quit=pygame.draw.rect(screen,(150,150,150),button_quit)
    text_surf =base_font.render("Quit", True, (0,0,0))
    screen.blit(text_surf, (button_quit.x+25,button_quit.y))

    btn_solve=pygame.draw.rect(screen,(150,150,150),button_solve)
    text_surf =base_font.render("Solve", True, (0,0,0))
    screen.blit(text_surf, (button_solve.x+20,button_solve.y))

    btn_hint=pygame.draw.rect(screen,(150,150,150),button_hint)
    text_surf =base_font.render("Hint", True, (0,0,0))
    screen.blit(text_surf, (button_hint.x+25,button_hint.y))

    for i in range(10):
        if i%3==0:
            pygame.draw.line(screen,(0,0,0),(50+50*i,50),(50+50*i,500),5)
            pygame.draw.line(screen,(0,0,0),(50,50+50*i),(500,50+50*i),5)
        else:   
            pygame.draw.line(screen,(0,0,0),(50+50*i,50),(50+50*i,500),2)
            pygame.draw.line(screen,(0,0,0),(50,50+50*i),(500,50+50*i),2)
    for g in range(0,9):
        for i in range(0,9):
            if board_to_solve[g][i]!=0:
                value=base_font.render(str(board_to_solve[g][i]),True,color_of_numbers)
                place_x=((i+1)*50+20)
                place_y=((g+1)*50+15) 
                screen.blit(value,(place_x,place_y))

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
                    if check_mistakes(pos,temp_board):
                        anwser='Success'
                        active=False
                    else:
                        mistake+=1
                        anwser='Wrong'
                        active=False

                    if check_if_solved(temp_board):
                        value_end=base_font.render(f"Congratulation! You made {mistake} mistakes",True,(0,0,0))
                        screen.blit(value_end,(30,545))

                    active=False

                if event.key == pygame.K_DELETE:
                    temp_board=clear_board(temp_board)
                    key =0     

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if place_clicked(pos):
                if temp_board[(pos[1]//50)-1][(pos[0]//50)-1]!=0:
                    key=temp_board[pos[1]//50-1][pos[0]//50-1]
                else:
                    key=0
                active=True
                previous_pos=pos    
            elif restart_clicked(pos):
                active=False
                temp_board=clear_board(temp_board)
                mistake=0
                key =0  
                start=time.time()
            elif quit_clicked(pos):
                pygame.quit()
                sys.exit()
            elif solve_clicked(pos):
                active=False
                temp_board=solve_place(pos)
            elif hint_clicked(pos):
                active=False
                if place_clicked(previous_pos):
                    temp_board=hint(previous_pos,temp_board)
                    
            else:
                active=False

    if active:
        rectangle=pygame.draw.rect(screen,(125,125,125),(((pos[0]//50)*50)+width_line,((pos[1]//50)*50)+width_line,50-width_line,50-width_line))
        temp_board=checked(key)    
    else:
        key=' '   

    for g in range(0,9):
        for i in range(0,9):
            if temp_board[g][i]!=0:
                value1=base_font.render(str(temp_board[g][i]),True,(0,0,0))
                place_x=((i+1)*50+20)
                place_y=((g+1)*50+15) 
                screen.blit(value1,(place_x,place_y))
    
    value_mistake=base_font.render(anwser,True,(0,0,0))
    screen.blit(value_mistake,(50,20)) 

    if check_if_solved(temp_board):
        value_end=base_font.render(f"Congratulation! You made {mistake} mistakes",True,(0,0,0))
        screen.blit(value_end,(30,545))

    text = base_font.render("Time:" + format_time(play_time), 1, (0,0,0))
    screen.blit(text, (350, 20))  

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

