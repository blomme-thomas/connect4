import game
import numpy as np
import random

game = game.Game()

# t = np.zeros((6,7))

# np.savetxt("matrix.txt", t)

for i in range(1000):
    game.grid.values = np.zeros((6,7))
    game.run()