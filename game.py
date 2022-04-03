import grid

class Game:
    def __init__(self):
        self.grid = grid.Grid()
        
        
    def run(self):
        while(1):

            player1 = input()
            if (player1 == "q"):
                break
            i = 5
            while(self.grid.values[i,int(player1)] != 0):
                i -= 1
            self.grid.values[i,int(player1)] = 1

            if (self.check_state() == 1):
                print("player 1 win")
                self.grid.display()
                break

            player2 = input()
            if (player2 == "q"):
                break
            i = 5
            while(self.grid.values[i,int(player2)] != 0):
                i -= 1
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
        state = -1
        for i in range(5,-1,-1):
            for j in range(5):
                if self.grid.values[i,j] == 0:
                    continue
                if (i>2):
                    if (self.grid.values[i,j] == self.grid.values[i-1,j] == self.grid.values[i-2,j] == self.grid.values[i-3,j] == 1):
                        state = 1
                        break
                    if (self.grid.values[i,j] == self.grid.values[i-1,j] == self.grid.values[i-2,j] == self.grid.values[i-3,j] == 2):
                        state = 2
                        break
                if (j<4):
                    if (self.grid.values[i,j] == self.grid.values[i,j+1] == self.grid.values[i,j+2] == self.grid.values[i,j+3] == 1):
                        state = 1
                        break
                    if (self.grid.values[i,j] == self.grid.values[i,j+1] == self.grid.values[i,j+2] == self.grid.values[i,j+3] == 2):
                        state = 2  
                        break
                if (i>2):
                    if (j<=3):
                        if (self.grid.values[i,j] == self.grid.values[i-1,j+1] == self.grid.values[i-2,j+2] == self.grid.values[i-2,j+3] == 1):
                            state = 1
                            break
                        if (self.grid.values[i,j] == self.grid.values[i-1,j+1] == self.grid.values[i-2,j+2] == self.grid.values[i-2,j+3] == 2):
                            state = 2
                            break
                    if (j>=3):
                        if (self.grid.values[i,j] == self.grid.values[i-1,j-1] == self.grid.values[i-2,j-2] == self.grid.values[i-2,j-3] == 1):
                            state = 1
                            break
                        if (self.grid.values[i,j] == self.grid.values[i-1,j-1] == self.grid.values[i-2,j-2] == self.grid.values[i-2,j-3] == 2):
                            state = 2
                            break
        return state
