# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:58:24 2021

@author: Roman Makarov
"""
import random
import copy
import time
from colorama import Fore, Style

class settings:
    rows = 19
    columns = 40
    
class cell:
    """
    Describes cell behaviour
    
    """
    alive = False
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def decide_life(self, b):
        self.alive = b

    def see_life(self):
        return self.alive
        
    def update(self):
        count = check_neighbors(self.x, self.y)
        # basically rules of cellular automata, neatly packed
        if not self.alive and count == 3:
            self.alive = True
        elif self.alive:
            if count != 2 and \
                count != 3:
                    self.alive = False
                   
    def __str__(self):
        return f'{Fore.CYAN}%d{Style.RESET_ALL}' % 0 if self.alive \
            else f'{Fore.BLACK}%d{Style.RESET_ALL}' % 0
    
def instantiate():
    """
    Creates a grid with set number of columns and rows and 
    fills it with randomized pattern of cells

    Returns
    -------
    None.

    """
    global grid
    
    x = 0
    for i in range(settings.rows):
        y = 0
        for j in range(settings.columns):
            grid[x, y] = cell(x, y)
            grid[x, y].decide_life(True if random.randint(0, 1) else False)
            # ^replaces thing below, using little trick I found: if (int) == True ""if int != 0""
            # if b == 1:
            #     grid[x, y].decide_life(True)
            # else:
            #     grid[x, y].decide_life(False)
            y += 1
        x += 1
        
    x = 0
    for i in range(settings.rows):
        y = 0
        for j in range(settings.columns):
            print(str(grid[x, y]), end = ' ')
            y += 1
        print()
        x += 1
        
def evolution():
    """
    Updates a grid using following set of rules (rules are coded into cells themselves):
    1. Any live cell with two or three live neighbours survives.
    2. Any dead cell with three live neighbours becomes a live cell.
    3. All other live cells die in the next generation. Similarly, all other dead cells stay dead. 

    Returns
    -------
    None.

    """
    global grid
    temp = copy.deepcopy(grid)
    
    x = 0
    for i in range(settings.rows):
        y = 0
        for j in range(settings.columns):
            temp[x, y].update()
            y += 1
        x += 1
        
    x = 0
    for i in range(settings.rows):
        y = 0
        for j in range(settings.columns):
            print(str(temp[x, y]), end = ' ')
            y += 1
        print()
        x += 1
    
    grid = temp.copy()
    
def automate():
    """
    automates evolution() using infinite loop

    Returns
    -------
    None.

    """
    while True:
        evolution()
        print()
        time.sleep(1)

def check_neighbors(x, y):
    """
    finds alive cell neighbors

    Parameters
    ----------
    x : cell X coordinate.
    y : cell Y coordinate.

    Returns
    -------
    count : amount of alive cell neighbors.

    """
    global grid
    count = 0    
    for i in range(0, 3):
        for j in range(0, 3):
            if not (i == 1 and j == 1): # don't want to count cell as its own neighbour
                count += 1 if grid.get((x - 1 + i, y - 1 + j), illegal_cell).see_life() \
                    else 0
                    
    # ^replaces this monstrocity below
    # count += 1 if grid.get((x, y + 1), illegal_cell).see_life() else 0
    # count += 1 if grid.get((x, y - 1), illegal_cell).see_life() else 0
    # count += 1 if grid.get((x - 1, y), illegal_cell).see_life() else 0
    # count += 1 if grid.get((x + 1, y), illegal_cell).see_life() else 0
    # count += 1 if grid.get((x - 1, y - 1), illegal_cell).see_life() else 0
    # count += 1 if grid.get((x + 1, y - 1), illegal_cell).see_life() else 0
    # count += 1 if grid.get((x - 1, y + 1), illegal_cell).see_life() else 0
    # count += 1 if grid.get((x + 1, y + 1), illegal_cell).see_life() else 0
    # should be much faster than 8 try catch blocks and looks much cleaner, too
                    
    return count

def main():
    pass

if __name__ == '__main__':
    grid = {}
    illegal_cell = cell(-1, -1)
    main()