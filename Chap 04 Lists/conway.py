# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Creat a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randit(0, 1) == 0;
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.
