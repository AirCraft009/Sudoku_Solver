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
        self.CalcDistances()
        self.calc_Cols()
        self.calc_Rows()
        self.beginn = self.find_first_empty_space()
        self.solved = False
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
    def Solve(self):
        space = self.find_first_empty_space()
        if space == -1:
            return True
        for num in range(1, 10):
            if self.placeNumber(space, num):
                if self.Solve():
                    return True
                self.board[space] = -1
        return False
    
    def writeToScreen(self, text, cordx, cordy, window, txtF):
        txt = txtF.render(text, True, "white")
        window.blit(txt, (cordx, cordy))
        pygame.display.flip()
            
                    
if __name__ == "__main__":
    sudoku_field = "xxxx7x3149x1x2xxxxxxxxx7x9x3x8xx9x677x9xxx1x2x18x6x2x42xxx6x8x3xxxxxx7xxx3x2xxx9x"
    if(len(sudoku_field )!= 81):
        print(len(sudoku_field)) 
        raise Exception("Sudoku field must be 81 characters long")
    s = Sudoku(sudoku_field)
    start = time.time_ns()
    s.Solve()
    print("Time to solve: " + str((time.time_ns()-start)/1e6)+ " ms")
    print(s.board)
    print(s.generateFillString())


