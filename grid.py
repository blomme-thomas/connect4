import numpy as np

class Grid:
    def __init__(self):
        self.values = np.zeros((6,7))

    def display(self):
        print(self.values)