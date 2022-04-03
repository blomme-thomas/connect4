from pygame import init
import numpy as np

class Grid:
    def __init__(self):
        self.values = np.zeros((7,6))

    def display(self):
        print(self.values)