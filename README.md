# Console-Game-of-Life
A cellular automata, known as "Conway's Game of Life", made in Python and visualised in IPython Console. Gif preview in the end.

A simplistic (under 100 lines of code without comments and docstrings) implementation of a well-known cellular automata (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

How it is done:
1) There is a class 'cell', defining individual cell behaviour. It has following properties: boolean 'alive', indicating if a cell is alive or not; int x and y, which represent 'coordinates' of cells.
There is a setter and a getter for 'alive' property.
To instantiate 'cell', you need to provide x and y arguments.
There is an update() method, which changes 'alive' property based on a count of cells 'neighbours' in 'grid'.
__str__ is redefined to return colored zero.
2) There is a global scope dictionary 'grid', which is filled with key-value pairs - tuple(x, y) and an object of 'cell'
3) instantiate() fills 'grid' with set number of 'rows' and 'columns' (they are stored in a class 'settings') and randomly assigns 'cell' instances 'alive' property (either True or False). 
By changing range and places of True and False in the line 64, you can get different alive/dead coefficient.
4) evolution() creates a copy of 'grid' and calls update() on all of its cells, using original 'grid' as a reference for cell neighbours (a copy is needed for proper execution of the code).
5) automate() calls evolution() in an endless loop with a small cooldown, which creates an illusion of a cellular automata in your IPython console. p.s. keyboard interruption in python - Ctrl + C
6) I imported Colorama (https://pypi.org/project/colorama/) to change the color of printed values, so for code to work on your machine you need to have it installed.

What I learned:
1) Difference between shallow copy and deep copy.
3) Few neat little 'tricks', that you can find in comments.
3) I suspect that print() is slow, so to get huge grid working fast you're better off using some sort of GUI library.

End result looks like this:

![Alt Text](https://s4.gifyu.com/images/ezgif-3-0b802657f083.gif)
