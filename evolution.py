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
        if not self.alive and count == 3:
            self.alive = True
        elif self.alive:
            if count != 2 and \
                count != 3:
                    self.alive = False
                   
    def __str__(self):
        return '0'
    
def instantiate():
    """
    Fills a grid with set number of columns and rows and 
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
            b = random.randint(0, 1)
            if b == 1:
                grid[x, y].decide_life(True)
            else:
                grid[x, y].decide_life(False)
            y += 1
        x += 1
        
    x = 0
    for i in range(settings.rows):
        y = 0
        for j in range(settings.columns):
            if grid[x, y].see_life():
                print(f'{Fore.CYAN}%d{Style.RESET_ALL}' % int((str(grid[x, y]))), end=' ')
            else:
                print(f'{Fore.BLACK}%d{Style.RESET_ALL}' % int((str(grid[x, y]))), end=' ')
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
            if temp[x, y].see_life():
                print(f'{Fore.CYAN}%d{Style.RESET_ALL}' % int((str(temp[x, y]))), end=' ')
            else:
                print(f'{Fore.BLACK}%d{Style.RESET_ALL}' % int((str(temp[x, y]))), end=' ')
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
    checks amount of alive cell neighbors

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
    try:
        if grid[x - 1, y].see_life():
            count += 1
    except KeyError:
        pass
    try:
        if grid[x - 1, y - 1].see_life():
            count += 1
    except KeyError:
        pass
    try:
        if grid[x - 1, y + 1].see_life():
            count += 1
    except KeyError:
        pass
    try:
        if grid[x, y + 1].see_life():
            count += 1
    except KeyError:
        pass
    try:
        if grid[x, y - 1].see_life():
            count += 1
    except KeyError:
        pass
    try:
        if grid[x + 1, y].see_life():
            count += 1
    except KeyError:
        pass
    try:
        if grid[x + 1, y - 1].see_life():
            count += 1
    except KeyError:
        pass
    try:
        if grid[x + 1, y + 1].see_life():
            count += 1
    except KeyError:
        pass
    return count

def main():
    pass

if __name__ == '__main__':
    grid = {}
    main()