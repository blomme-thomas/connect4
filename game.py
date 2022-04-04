import grid

class Game:
    def __init__(self):
        self.grid = grid.Grid()
        self.state = 0        
        
    def run(self):
        while(1):
            while(1):
                player1 = input()
                if (int(player1)>6 or int(player1)<0):
                    print("coup impossible")
                    continue
                if (player1 == "q"):
                    break
                i = 5
                while(self.grid.values[i,int(player1)] != 0 and i>=0):
                    i -= 1
                if (i<0):
                    print("coup impossible")
                else:
                    break
            self.grid.values[i,int(player1)] = 1

            if (self.check_state() == 1):
                print("player 1 win")
                self.grid.display()
                break
            
            self.grid.display()

            while(1):
                player2 = input()
                if (int(player2)>6 or int(player2)<0):
                    print("coup impossible")
                    continue
                if (player2 == "q"):
                    break
                i = 5
                while(self.grid.values[i,int(player2)] != 0 and i>=0):
                    i -= 1
                if (i<0):
                    print("coup impossible")
                else:
                    break
            self.grid.values[i,int(player2)] = 2

            if (self.check_state() == 2):
                print("player 2 win")
                self.grid.display()
                break

            if (self.check_state() == 0):
                print("egality")
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