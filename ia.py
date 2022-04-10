import game
import numpy as np
import qlearning
import random

def coup_posssible(grid):
    coups = np.zeros(7)
    for i in range(7):
        h = 5
        while grid[h, i] != 0 and h!=0:
            h-=1
        if h == 0:
            coups[i] = -1
        else:
            coups[i] = h
    return coups

def meilleur_coup(grid,qlearning):
    coups = coup_posssible(grid)
    max = 0
    m = 0
    for i in range(7):
        if coups[i] != -1:
            if max<=qlearning[int(coups[i]), i]:
                max = qlearning[int(coups[i]), i]
                m = i
    
    return int(coups[m]), m

def jouer(game,player,qlearning):
    c = meilleur_coup(game.grid.values, qlearning)
    game.place_coin(c[1],player)
    return c