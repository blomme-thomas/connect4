import grid
import numpy as np

def update(r, f, grid):
    n, m = grid.shape
    for i in range(n):
        for j in range(m):
            max = grid[i, j]
            if i>0:
                if max<(r+f*grid[i-1,j]):
                    max = r+f*grid[i-1,j]
                if j>0:
                    if max<(r+f*grid[i-1,j-1]):
                        max = r+f*grid[i-1,j-1]
                if j<n-1:
                    if max<(r+f*grid[i-1,j+1]):
                        max = r+f*grid[i-1,j+1]
            if i<n-1:
                if max<(r+f*grid[i+1,j]):
                    max = r+f*grid[i+1,j]
                if j>0:
                    if max<(r+f*grid[i+1,j-1]):
                        max = r+f*grid[i+1,j-1]
                if j<n-1:
                    if max<(r+f*grid[i-1,j+1]):
                        max = r+f*grid[i-1,j+1]
            if j>0:
                if max<(r+f*grid[i,j-1]):
                    max = r+f*grid[i,j-1]
            if j<m-1:
                if max<(r+f*grid[i,j+1]):
                    max = r+f*grid[i,j+1]
            grid[i,j] = max
    return

def update_case(r, f, grid, i, j):
    n, m = grid.shape
    max = grid[i, j]
    if i>0:
        if max<(r+f*grid[i-1,j]):
            max = r+f*grid[i-1,j]
        if j>0:
            if max<(r+f*grid[i-1,j-1]):
                max = r+f*grid[i-1,j-1]
        if j<n-1:
            if max<(r+f*grid[i-1,j+1]):
                max = r+f*grid[i-1,j+1]
    if i<n-1:
        if max<(r+f*grid[i+1,j]):
            max = r+f*grid[i+1,j]
        if j>0:
            if max<(r+f*grid[i+1,j-1]):
                max = r+f*grid[i+1,j-1]
        if j<n-1:
            if max<(r+f*grid[i-1,j+1]):
                max = r+f*grid[i-1,j+1]
    if j>0:
        if max<(r+f*grid[i,j-1]):
            max = r+f*grid[i,j-1]
    if j<m-1:
        if max<(r+f*grid[i,j+1]):
            max = r+f*grid[i,j+1]
    grid[i,j] = max
    return



