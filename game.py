import grid

class Game:
    def __init__(self):
        self.grid = grid.Grid()
        self.state = 0        
        
    def run(self):
        while(1):
            c = input()
            self.place_coin(c,1)
            if (self.check_state() == 1):
                print("player 1 win")
                self.grid.display()
                break

            c = input()
            self.place_coin(c,2)
            if (self.check_state() == 2):
                print("player 2 win")
                self.grid.display()
                break

            if (self.check_state() == 0):
                print("Draw")
                self.grid.display()
                break

            self.grid.display()
            
            

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


