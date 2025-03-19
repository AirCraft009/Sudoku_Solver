import numpy as np
import time
import pygame


class Sudoku():
    def __init__(self, fillString):
        self.board = {}
        self.fillBoard(fillString)
        self.distanceL = {}
        self.distanceR = {}
        self.distanceT = {}
        self.distanceB = {}
        self.groups = [[],[],[],[],[],[],[],[],[]]
        self.rows = [[],[],[],[],[],[],[],[],[]]
        self.cols = [[],[],[],[],[],[],[],[],[]]
        self.hardEdges = []
        for x in self.board:
            if self.board[x] == -1:
                continue
            self.hardEdges.append(x)
        self.pastTries = {}
        for x in range(81):
            self.pastTries[x] = []
        self.CalcDistances()
        self.calc_Cols()
        self.calc_Rows()
        self.beginn = self.find_first_empty_space()
        self.solved = False
        self.last_start = -1
        self.last_end = -1
        self.high = self.beginn
        print(self.beginn)
        
    def fillBoard(self, fillString):
        for i in range(81):
            if fillString[i] == "x":
                self.board[i] = -1
            else:
                self.board[i] = int(fillString[i])
    def generateFillString(self):
        fill = ""
        for i in range(81):
            if self.board[i] == -1:
                fill += "x"
            else:
                fill += str(self.board[i])
        return fill
                
                
    def CalcDistances(self):
        line = -3
        adder = 0
        for i in range(81):
            self.distanceL[i] = i%9
            self.distanceR[i] = 8-self.distanceL[i]
            self.distanceT[i] = i//9
            self.distanceB[i] = 8-self.distanceT[i]
        for i in range(9):
            for x in range(3):
                for y in range(3):
                    self.groups[i].append(27*(i//3)+3*(i%3)+9*x+y)
    
    def find_Index_Group(self, space):
        return self.groups.index(self.find_Group(space))
    
    def calc_Cols(self):
        for x in range(9):
            for y in range(9):
                self.cols[x].append(x+(9*y))
    
    def calc_Rows(self):
        for x in range(9):
            for y in range(9):
                self.rows[x].append(y+9*x)
    
    def find_Group(self, space):
        for group in self.groups:
            if space in group:
                return group
            
    def get_NumSpace(self, space):
        return self.board[space]
        
    def find_duplicates_In_X(self, space: int, num: int, cross: iter):
        """
        finds if the given num in the parameters is 
        already in the given section(cross):

        Args:
            space (_type_): _description_
            num (_type_): _description_
            cross (_type_): _description_
        """
        for spaceC in cross:
            if spaceC == space:
                continue
            if self.get_NumSpace(spaceC) == num:
                return True
        return False
    
    def checkNumber(self, space, num):
        group = self.find_Group(space)
        if space in self.hardEdges:
            return False
        if self.find_duplicates_In_X(space, num, group):
            return False
        if self.find_duplicates_In_X(space, num, self.rows[space//9]):
            return False
        if self.find_duplicates_In_X(space, num, self.cols[space%9]):
            return False
        return True
        
        
    
    def placeNumber(self, space, num: int):
        if(self.checkNumber(space, num)):
            self.board[space] = num
            return True
        return False
    
    def find_first_empty_space(self):
        for space in range(81):
            if self.get_NumSpace(space) == -1 and space not in self.hardEdges:
                return space
        return -1
    
    def find_previous(self, space):
        start = space
        if space != self.beginn:
            space -= 1
        while True:
            if space in self.hardEdges and space > self.beginn:
                space -= 1
            else:
                return space
    def Solve(self, pause, screen=None, txtF=None):
    
        space = self.find_first_empty_space()
        if space == -1:
            return True
        for num in range(1, 10):
            if self.placeNumber(space, num):
                if screen != None:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            break
                    pygame.display.update()
                    self.writeToScreen(str(num), space%9*100+50, space//9*100+25, screen, txtF)
                time.sleep(pause)  
                if self.Solve(pause):
                    return True
                self.board[space] = -1
        return False
    
    def writeToScreen(self, text, cordx, cordy, window, txtF):
        txt = txtF.render(text, True, "white")
        window.blit(txt, (cordx, cordy))
        pygame.display.flip()
            
                    
if __name__ == "__main__":
    sudoku_field = "28x5xxxxxxxxxx91xxxx47xxxx24x19xx2xxxxxx7xxxxxx5xx64x78xxxx79xxxx31xxxxxxxxxx8x65"
    print(len(sudoku_field)) 
    s = Sudoku(sudoku_field)
    s.Solve(0)
    print(s.board)
    print(s.generateFillString())


