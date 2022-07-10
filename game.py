import pygame, sys
import numpy as np
import controller as c
import board as b
import ai

pygame.init()

WIDTH = 600
HEIGHT = 600
COLOR = (225, 225, 225)
LINE_COLOR = (200, 200, 200)
LINE_WIDTH = 7
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 5
FIGURE_COLOR = (255, 255, 255)
CROSS_COLOR = (0, 0, 0)
global USER
USER = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")
screen.fill(COLOR)

def draw_lines():
    # horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600,200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600,400), LINE_WIDTH)
    # vertical
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200,600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400,600), LINE_WIDTH)
def draw_figures():
    for row in range(3):
        for col in range(3):
            if(b.getPiece(row,col) == "O"):
                pygame.draw.circle(screen, FIGURE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif(b.getPiece(row,col) == "X"):
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + 55, row * 200 + 200 - 55), (col * 200 + 200 - 55, row * 200 + 55), LINE_WIDTH)
                pygame.draw.line( screen, CROSS_COLOR, (col * 200 + 55, row * 200 + 55), (col * 200 + 200 - 55, row * 200 + 200 - 55), LINE_WIDTH)
                
draw_lines()
gameOver = False
while(True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
        if(event.type == pygame.MOUSEBUTTONDOWN and USER == 0):
            mx = event.pos[0]
            my = event.pos[1]

            c_row = int(my // 200)
            c_col = int(mx // 200)
            if(c.isValid(USER, c_row, c_col)):
                b.updateBoard("O", c_row, c_col)
                winner = c.check_winner()
                draw = c.check_draw()
                if(winner == 0 or winner == 1):
                    c.display_winner()
                elif(draw == False):
                    print("It's a draw!")
                USER = 1
        elif(USER == 1):
            ai.ai_move()
            winner = c.check_winner()
            draw = c.check_draw()
            if(winner == 0 or winner == 1):
                c.display_winner()
            elif(draw == False):
                print("It's a draw!")
            USER = 0
        draw_figures()
    draw_figures
    pygame.display.update()