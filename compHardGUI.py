from compEasyGUI import CompEasyGUI
import customtkinter as customtkinter
import random
import math


class CompHardGUI(CompEasyGUI):
    def __init__(self, parent,main):
        super().__init__(parent, main)
        self.indexesBttn = {
            (0, 0): 0,
            (0, 1): 1,
            (0, 2): 2,
            (1, 0): 3,
            (1, 1): 4,
            (1, 2): 5,
            (2, 0): 6,
            (2, 1): 7,
            (2, 2): 8,
        }

    #for move computer when his turn
    def comp_move(self,board): 

        if self.compFlag==False  :
            
            firsMove =self.firstMove()

            if firsMove == True:
                ran_zero = [(i, j) for i, row in enumerate(self.board) for j, value in enumerate(row) if value == 0]
                ran = random.choice(ran_zero)
                bttn = self.buttons[ran[0]][ran[1]]
                indx = self.indexesBttn.get(ran, None)
            
                x =  bttn.winfo_x()
                y = bttn.winfo_y()
            
                self.press(indx+1,x,y)

            else:    
                if self.player1.icon=="X":
                    score,move,res = self.MinMaxAlgo(self.board,1,True)
                    self.print(self.board, 1)
                else :  
                    score,move,res = self.MinMaxAlgo(self.board,-1,True)  
                    self.print(self.board, -1)

                x1,y1=move
                indx = self.indexesBttn.get(move, None)
                bttn = self.buttons[x1][y1]
                x =  bttn.winfo_x()
                y = bttn.winfo_y()

                self.flash_bttn(bttn,indx,x,y)
                
   
    #mimMax Alogrthim
    def MinMaxAlgo(self,board,player,max):
        
        x = self.stateBoard(board, player)
        if x is not None and x == 1: return x,None,["Win"]
        if x is not None and x == -1: return x,None,["Lose"]
        if x is not None and x == 0: return x,None, ["Draw"]

        if max: bestScore = -math.inf
        else: bestScore = math.inf

        if player == -1: comp = 1
        else: comp = -1

        st=[]
        allMoves = self.allMove(board, player if max else comp)

        bestMove = None
        for brd, coord in allMoves:
            nextScore,nextMove,res = self.MinMaxAlgo(brd, player, not max)
            
            for r in res:
                if r not in st: st.append(r)
    
            if max and nextScore > bestScore:
                bestScore = nextScore
                bestMove = coord
            if not max and nextScore < bestScore:
                bestScore = nextScore
                bestMove = coord
     
        return bestScore, bestMove,st

    #to check if its a first move 
    def firstMove(self):
        icon = self.player2.icon
    
        if icon == "X" and not self.answeO :return True
        elif icon == "O" and not self.answeX:return True
        else: return False
            
   
   #get all board where player can move
    def allMove(self,board, player):
        arr = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    brd = [x[:] for x in board]
                    brd[i][j] = player   
                    arr.append((brd, (i, j)))

        return arr
    
    #print on button
    def print(self,board, player):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    brd = [row[:] for row in board]
                    brd[i][j] = player
                    z, x,res = self.MinMaxAlgo(brd, player, False)
                    self.buttons[i][j].configure(text=f"{' '.join(res)}")
    
    #get state of board, win lose draw
    def stateBoard(self,board, player):
        end, plyr = self.End(board)
        if  end == False: return None
        if plyr == 0: return 0
        if plyr == player: return 1
        else: return -1
    
    #end game, whose win 
    def End(self,board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                return True, board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != 0:
                return True, board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != 0:
            return True, board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != 0:
            return True, board[0][2]

        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return False, 0
        return True, 0
    

    #to make selected button flashing
    def flash_bttn(self,button,indx,x,y):

        button.after(100, lambda: button.config(fg="white"))
        button.after(300, lambda: button.config(fg="red"))
        button.after(600, lambda: button.config(fg="white"))
        button.after(800, lambda: button.config(fg="red"))
        button.after(1000, lambda: button.config(fg="white"))
        button.after(1200, lambda: button.config(fg="red"))
        button.after(1500, lambda: button.config(fg="white"))
        button.after(1900, lambda: button.config(fg="red"))
        button.after(2400, lambda: button.config(fg="white"))
        button.after(3000, lambda: button.config(fg="red"))
        button.after(3000,lambda:self.press(indx+1,x,y))