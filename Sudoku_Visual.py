import pygame
import Sudoku
import threading

pygame.init()

window = pygame.display.set_mode((900, 900))
txtF = pygame.sysfont.SysFont("Arial", 40)
pygame.display.set_caption("Sudoku Solver")

window.fill("teal")

def writeToScreen(text, cordx, cordy):
    txt = txtF.render(text, True, "white")
    window.blit(txt, (cordx, cordy))

def drawBoard():
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(window, "grey", (i*100, j*100, 100, 100), 2)
            pygame.display.flip()
            
def fill_board(fillString):
    for i in range(81):
        if fillString[i] == "x":
            continue
        else:
            writeToScreen(fillString[i], i%9*100+50, i//9*100+25)
drawBoard()   
f_string = "28x5xxxxxxxxxx91xxxx47xxxx24x19xx2xxxxxx7xxxxxx5xx64x78xxxx79xxxx31xxxxxxxxxx8x65"
fill_board(f_string)

sud = Sudoku.Sudoku(f_string)
sud.Solve(0.001, window, txtF)