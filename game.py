import grid
import ia
import numpy as np
import qlearning
import random

class Game:
    
    def __init__(self):
        self.grid = grid.Grid()
        self.state = 0        
        self.q = np.loadtxt("matrix.txt")

    def run(self):
        while(1):
            ia1 = ia.jouer(self, 1, self.q)
            qlearning.update_case(0.1,0.6,self.q,ia1[0],ia1[1])
            
            if (self.check_state() == 1):
                qlearning.update_case(1,0.6,self.q,ia1[0],ia1[1])
                print("player 1 win")
                np.savetxt("matrix.txt", self.q)
                break

            c = self.coup_possible()
            print(c)
            self.place_coin(random.choice(c),2)
            
            if (self.check_state() == 2):
                print("player 2 win")
                np.savetxt("matrix.txt", self.q)
                break

            if (self.check_state() == 0):
                print("Draw")
                np.savetxt("matrix.txt", self.q)
                break

            np.savetxt("matrix.txt", self.q)
            
            
            

    def check_state(self):
        self.state = -1
        for i in range(5,-1,-1):
            for j in range(5):
                
                if self.grid.values[i,j] == 0:
                    continue
                if (i>2):
                    if (self.grid.values[i,j] == self.grid.values[i-1,j] == self.grid.values[i-2,j] == self.grid.values[i-3,j] == 1):
                        self.state = 1
                        break
                    if (self.grid.values[i,j] == self.grid.values[i-1,j] == self.grid.values[i-2,j] == self.grid.values[i-3,j] == 2):
                        self.state = 2
                        break
                if (j<4):
                    if (self.grid.values[i,j] == self.grid.values[i,j+1] == self.grid.values[i,j+2] == self.grid.values[i,j+3] == 1):
                        self.state = 1
                        break
                    if (self.grid.values[i,j] == self.grid.values[i,j+1] == self.grid.values[i,j+2] == self.grid.values[i,j+3] == 2):
                        self.state = 2  
                        break
                if (i>2):
                    if (j<=3):
                        if (self.grid.values[i,j] == self.grid.values[i-1,j+1] == self.grid.values[i-2,j+2] == self.grid.values[i-3,j+3] == 1):
                            self.state = 1
                            break
                        if (self.grid.values[i,j] == self.grid.values[i-1,j+1] == self.grid.values[i-2,j+2] == self.grid.values[i-3,j+3] == 2):
                            self.state = 2
                            break
                    if (j>=3):
                        if (self.grid.values[i,j] == self.grid.values[i-1,j-1] == self.grid.values[i-2,j-2] == self.grid.values[i-3,j-3] == 1):
                            self.state = 1
                            break
                        if (self.grid.values[i,j] == self.grid.values[i-1,j-1] == self.grid.values[i-2,j-2] == self.grid.values[i-3,j-3] == 2):
                            self.state = 2
                            break
        return self.state

    def place_coin(self,column,player):
        while(1):
            print(player)
            if (int(column)>6 or int(column)<0):
                print("coup impossible")
                continue
            if (column == "q"):
                break
            i = 5
            while(self.grid.values[i,int(column)] != 0 and i>=0):
                i -= 1
            if (i<0):
                print("coup impossible")
            else:
                break

        if (player == 1):
            self.grid.values[i,int(column)] = 1
        elif (player == 2):
            self.grid.values[i,int(column)] = 2           


    def coup_possible(self):
        c = []
        for j in range(7):
            i = 5
            while self.grid.values[i, j] != 0 and i!=-1:
                i-=1
            if i != -1:
                c.append(j)
        return c