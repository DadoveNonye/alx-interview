#!/usr/bin/python3
""" function def island_perimeter(grid): that returns the perimeter of the island"""

def island_perimeter(grid):
    """ Returns the perimeter of the island"""
    if not grid or not grid[0]:
        return 0
    
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check top cell
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check bottom cell
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check left cell
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check right cell
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1
    
    return perimeter
