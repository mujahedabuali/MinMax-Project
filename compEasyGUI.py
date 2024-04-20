from friendGUI import FriendGUI
import customtkinter as customtkinter
import tkinter as tk
from pygame import mixer
from PIL import Image,ImageTk
import random
from CTkMessagebox import CTkMessagebox

class CompEasyGUI(FriendGUI):
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


    def windowName(self):
        namesWindow =customtkinter.CTkToplevel(self)
        namesWindow.title("Players Name")
        namesWindow.geometry("450x250")
        namesWindow.resizable(False, False)
        def do_nothing():
         pass
        namesWindow.protocol("WM_DELETE_WINDOW", do_nothing)
        
        self.bgIMG1 = Image.open("icons/background.jpg").resize((450, 250))
        self.bg_image1 = ImageTk.PhotoImage(self.bgIMG1)

        canvas = customtkinter.CTkCanvas(namesWindow, width=450, height=250)
        canvas.pack(side="top",fill="both",expand=True)
        canvas.create_image(0, 0, anchor=customtkinter.NW, image=self.bg_image1)
        
        center_x = int(700)
        center_y = int(350)
        namesWindow.geometry(f"+{center_x}+{center_y}")

        self.IMG1 = Image.open("icons/athlete.png").resize((35, 35))
        self.player1_image = ImageTk.PhotoImage(self.IMG1)
        canvas.create_image(110, 15, anchor=customtkinter.NW, image=self.player1_image)

        canvas.create_text(240,35,text="Player Name:",fill="red",font=("Times New Roman",30,"italic"))

        entry = customtkinter.CTkEntry(canvas)
        entry.delete(0, customtkinter.END)
        entry.insert(0, "Player 1")
        entry.place(x=160,y=80)

        canvas.create_text(170,210,text="Rounds:",fill="White",font=("Times New Roman",28,"italic"))
        num_round = customtkinter.StringVar()
        combobox = customtkinter.CTkComboBox(master=canvas,width=5,variable=num_round,values=["1", "2", "3", "4", "5"])
        num_round.set("1")
        combobox.place(x=260,y=200)

        def names():
            mixer.init()
            mixer.music.load("sounds/click.wav")
            mixer.music.play()
            if entry.get() !="":
                self.canvas.itemconfig(self.playerName1, text=f"{entry.get()} :")
                self.canvas.itemconfig(self.MaxRoundLabel,text=f"/{num_round.get()}")
                self.MaxRound=num_round.get()
                namesWindow.destroy()

        submit_button = customtkinter.CTkButton(canvas, text="Done",command=names)
        submit_button.place(x=160,y=145)

        #for start button
    def start(self):
        mixer.init()
        mixer.music.load("sounds/start.wav")
        mixer.music.play()
        
        self.startFlag =True
        self.cont =0
        self.option.configure(state="disabled")
        self.board = [[0, 0, 0] for _ in range(3)]
        self.draw_count = [0]*9
        self.lose_count = [0]*9
        self.win_count = [0]*9
        
        #Make a window how start
        self.bgIMG2 = Image.open("icons/background.jpg").resize((450, 250))
        self.bg_image2 = ImageTk.PhotoImage(self.bgIMG2)
        
        startWindow =customtkinter.CTkToplevel(self)
        startWindow.title("Who Will Start??")
        startWindow.geometry("450x250")
        startWindow.resizable(False, False)
        def do_nothing():
         pass
        startWindow.protocol("WM_DELETE_WINDOW", do_nothing)

        center_x = int(700)
        center_y = int(350)
        startWindow.geometry(f"+{center_x}+{center_y}")

        canvas = customtkinter.CTkCanvas(startWindow, width=450, height=250)
        canvas.pack(side="top",fill="both",expand=True)
        canvas.create_image(0, 0, anchor=customtkinter.NW, image=self.bg_image2)
        canvas.create_text(220,50,text="Choose Who Will Start:",fill="White",font=("Times New Roman",30,"italic"))
        
        self.player1_image=customtkinter.CTkImage(Image.open("icons/athlete.png"),size=(35,35))
        self.player2_image=customtkinter.CTkImage(Image.open("icons/soccer-player.png"),size=(35,35))

        def choose(name1,name2,color):
            mixer.init()
            mixer.music.load("sounds/click.wav")
            mixer.music.play()
            #player 1 start
            if name1 == name1Split[0] :
                self.player1.name=name1
                self.player2.name=name2
                self.canvas.itemconfig(self.turnName, text=f"{self.player1.name}")
                self.canvas.itemconfig(self.turnName, fill=f"{color}")
                self.player1.icon=self.x_o.get()

                if self.x_o.get() =="X":
                    self.player2.icon="O"
                else :  self.player2.icon="X" 
            #computer start
            else:    
                self.player1.name=name2
                self.player2.name=name1
                self.canvas.itemconfig(self.turnName, text=f"{self.player2.name}")
                self.canvas.itemconfig(self.turnName, fill=f"{color}")
                self.player2.icon=self.x_o.get()

                if self.x_o.get() =="X":
                    self.player1.icon="O"
                else :  self.player1.icon="X" 

                self.state=self.x_o.get()
                self.comp_move(self.board)

            self.startBttn.configure(state="disabled")    
            startWindow.destroy()

        name1 = self.canvas.itemcget(self.playerName1, "text")
        name2 = self.canvas.itemcget(self.playerName2, "text")
        name1Split = name1.split(":")
        name2Split = name2.split(":")

        p1 = customtkinter.CTkButton(canvas,image=self.player1_image,compound="left",text=name1Split[0],command=lambda:choose(name1Split[0],name2Split[0],self.canvas.itemcget(self.playerName1, "fill")))
        p1.place(x=160,y=80)

        p2 = customtkinter.CTkButton(canvas,image=self.player2_image,compound="left",text=name2Split[0],command=lambda:choose(name2Split[0],name1Split[0],self.canvas.itemcget(self.playerName2, "fill")))
        p2.place(x=160,y=140)

        self.state=self.x_o.get()

    #for move computer when his turn
    def comp_move(self,board): 

        if self.compFlag==False  :
            
            ran_zero = [(i, j) for i, row in enumerate(board) for j, value in enumerate(row) if value == 0]
            ran = random.choice(ran_zero)
            bttn = self.buttons[ran[0]][ran[1]]

            indx = self.indexesBttn.get(ran, None)
            
            x =  bttn.winfo_x()
            y = bttn.winfo_y()
        
            self.press(indx+1,x,y)


    def press(self,num,x,y):
        if self.startFlag == True:
            mixer.init()
            mixer.music.load("sounds/buttonclick.wav")
            mixer.music.play()

            if  self.state=="X" :
                self.answeX.append(self.canvas.create_image(x+10, y+10, anchor=customtkinter.NW, image=self.x_image))
                if num == 1:
                    self.board[0][0]=-1
                    self.button1.destroy()
                elif num == 2:
                    self.board[0][1]=-1
                    self.button2.destroy()
                elif num == 3:
                    self.board[0][2]=-1
                    self.button3.destroy()
                elif num == 4:
                    self.board[1][0]=-1
                    self.button4.destroy()
                elif num == 5:
                    self.board[1][1]=-1
                    self.button5.destroy()
                elif num == 6:
                    self.board[1][2]=-1
                    self.button6.destroy()
                elif num == 7:
                    self.board[2][0]=-1
                    self.button7.destroy()
                elif num == 8:
                    self.board[2][1]=-1
                    self.button8.destroy()
                else:
                    self.board[2][2]=-1
                    self.button9.destroy()
                
                self.cont += 1
                self.state="O"
               

                if self.player1.icon=="X":
                    self.canvas.itemconfig(self.turnName, text=f"{self.player2.name}")
                    self.checkWin()
                    self.comp_move(self.board)
                else :   
                    self.canvas.itemconfig(self.turnName, text=f"{self.player1.name}")
                    self.checkWin()
            else:
                self.answeO.append(self.canvas.create_image(x+10, y+10, anchor=customtkinter.NW, image=self.o_image))
                if num == 1:
                    self.board[0][0]=1
                    self.button1.destroy()
                elif num == 2:
                    self.board[0][1]=1
                    self.button2.destroy()
                elif num == 3:
                    self.board[0][2]=1
                    self.button3.destroy()
                elif num == 4:
                    self.board[1][0]=1
                    self.button4.destroy()
                elif num == 5:
                    self.board[1][1]=1
                    self.button5.destroy()
                elif num == 6:
                    self.board[1][2]=1
                    self.button6.destroy()
                elif num == 7:
                    self.board[2][0]=1
                    self.button7.destroy()
                elif num == 8:
                    self.board[2][1]=1
                    self.button8.destroy()
                else:
                    self.board[2][2]=1
                    self.button9.destroy()
                
                self.cont += 1
                self.state="X"
               

                if self.player1.icon=="O":
                    self.canvas.itemconfig(self.turnName, text=f"{self.player2.name}")
                    self.checkWin()
                    self.comp_move(self.board)
                else :
                    self.canvas.itemconfig(self.turnName, text=f"{self.player1.name}")
                    self.checkWin()
        else :
                 mixer.init()
                 mixer.music.load("sounds/warn.wav")
                 mixer.music.play()

      #check if ended
    def checkWin(self):
        x=self.board_state(self.board)
       
        if(x==-1):
            if self.player1.icon == "X":
                mixer.init()
                mixer.music.load("sounds/win.wav")
                mixer.music.play()
                self.resLabel=self.canvas.create_text(790,700,text=f"{self.player1.name} Win!!!",fill="Red",font=("Times New Roman",45,"bold"))
                self.player1.points+=1
                self.canvas.itemconfig(self.res1, text=f"{self.player1.points}")
            else: 
                mixer.init()
                mixer.music.load("sounds/lose.wav")
                mixer.music.play()
                self.resLabel=self.canvas.create_text(790,700,text=f"The End, You Lost!!!",fill="Red",font=("Times New Roman",45,"bold"))  
                self.player2.points+=1 
                self.canvas.itemconfig(self.res2, text=f"{self.player2.points}")
                
            
            if(int(self.curRound)<int(self.MaxRound)):
                ww =int(self.MaxRound) // 2 +1
           
                flag = True

                if self.player1.points >= ww and self.player2.points < ww:
                    msg = CTkMessagebox(title="Warning Message!", message=f"{self.player1.name} Win!!!   Contineu ??",
                    icon="warning", option_1="Cancel", option_2="Contineu")
                    if msg.get()=="Contineu":
                        flag = True
                    if msg.get()=="Cancel":
                        flag = False    
                elif self.player2.points >= ww and self.player1.points < ww:
                    msg = CTkMessagebox(title="Warning Message!", message=f"{self.player2.name} Win!!!   Contineu ??",
                    icon="warning", option_1="Cancel", option_2="Contineu")
                    if msg.get()=="Contineu":
                        flag = True
                    if msg.get()=="Cancel":
                        flag = False   
               
                if flag == True:
                    self.nexBttn =customtkinter.CTkButton(self.canvas,text="Next Round!",width=160,height=35,command=self.nextRound) 
                    self.nexBttn.place(x=730,y=780)
            else:
                if self.player1.points>self.player2.points :
                    mixer.init()
                    mixer.music.load("sounds/win.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, {self.player1.name} Win!!!",fill="Red",font=("Times New Roman",45,"bold"))  
                elif self.player1.points<self.player2.points:
                    mixer.init()
                    mixer.music.load("sounds/lose.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, You Lost!!!",fill="Red",font=("Times New Roman",45,"bold"))      
                else:
                    mixer.init()
                    mixer.music.load("sounds/draw.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, its Draw!!!",fill="Red",font=("Times New Roman",45,"bold")) 
            
            self.cont = 0
            self.compFlag=True
            self.startFlag=False           
         
        if(x==1):

            if self.player1.icon == "O":
                mixer.init()
                mixer.music.load("sounds/win.wav")
                mixer.music.play()
                self.resLabel=self.canvas.create_text(790,700,text=f"{self.player1.name} Win!!!",fill="Red",font=("Times New Roman",45,"bold"))
                self.player1.points+=1
                self.canvas.itemconfig(self.res1, text=f"{self.player1.points}")
            else: 
                mixer.init()
                mixer.music.load("sounds/lose.wav")
                mixer.music.play()
                self.resLabel=self.canvas.create_text(790,700,text=f"The End, You Lost!!!",fill="Red",font=("Times New Roman",45,"bold"))  
                self.player2.points+=1 
                self.canvas.itemconfig(self.res2, text=f"{self.player2.points}")


            if(int(self.curRound)<int(self.MaxRound)):
                ww =int(self.MaxRound) // 2 +1
           
                flag = True

                if self.player1.points >= ww and self.player2.points < ww:
                    msg = CTkMessagebox(title="Warning Message!", message=f"{self.player1.name} Win!!!   Contineu ??",
                    icon="warning", option_1="Cancel", option_2="Contineu")
                    if msg.get()=="Contineu":
                        flag = True
                    if msg.get()=="Cancel":
                        flag = False    
                elif self.player2.points >= ww and self.player1.points < ww:
                    msg = CTkMessagebox(title="Warning Message!", message=f"{self.player2.name} Win!!!   Contineu ??",
                    icon="warning", option_1="Cancel", option_2="Contineu")
                    if msg.get()=="Contineu":
                        flag = True
                    if msg.get()=="Cancel":
                        flag = False   
               
                if flag == True:
                    self.nexBttn =customtkinter.CTkButton(self.canvas,text="Next Round!",width=160,height=35,command=self.nextRound) 
                    self.nexBttn.place(x=730,y=780)
            else:
                if self.player1.points>self.player2.points :
                    mixer.init()
                    mixer.music.load("sounds/win.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, {self.player1.name} Win!!!",fill="Red",font=("Times New Roman",45,"bold"))  
                elif self.player1.points<self.player2.points:
                    mixer.init()
                    mixer.music.load("sounds/lose.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, You Lost!!!",fill="Red",font=("Times New Roman",45,"bold"))      
                else:
                    mixer.init()
                    mixer.music.load("sounds/draw.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, its Draw!!!",fill="Red",font=("Times New Roman",45,"bold"))    
            
            self.compFlag=True
            self.startFlag=False
            self.cont = 0

        if (self.cont == 9 ):
            mixer.init()
            mixer.music.load("sounds/draw.wav")
            mixer.music.play()
            self.resLabel=self.canvas.create_text(790,700,text="DRAW!!!",fill="Red",font=("Times New Roman",45,"bold"))

            if(int(self.curRound)<int(self.MaxRound)):

                ww =int(self.MaxRound) // 2 +1
           
                flag = True

                if self.player1.points >= ww and self.player2.points < ww:
                    msg = CTkMessagebox(title="Warning Message!", message=f"{self.player1.name} Win!!!   Contineu ??",
                    icon="warning", option_1="Cancel", option_2="Contineu")
                    if msg.get()=="Contineu":
                        flag = True
                    if msg.get()=="Cancel":
                        flag = False    
                elif self.player2.points >= ww and self.player1.points < ww:
                    msg = CTkMessagebox(title="Warning Message!", message=f"{self.player2.name} Win!!!   Contineu ??",
                    icon="warning", option_1="Cancel", option_2="Contineu")
                    if msg.get()=="Contineu":
                        flag = True
                    if msg.get()=="Cancel":
                        flag = False   
               
                if flag == True:
                    self.nexBttn =customtkinter.CTkButton(self.canvas,text="Next Round!",width=160,height=35,command=self.nextRound) 
                    self.nexBttn.place(x=730,y=780)
            else :
                if self.player1.points>self.player2.points :
                    mixer.init()
                    mixer.music.load("sounds/win.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, {self.player1.name} Win!!!",fill="Red",font=("Times New Roman",45,"bold"))  
                elif self.player1.points<self.player2.points:  
                    mixer.init()
                    mixer.music.load("sounds/lose.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, You Lost!!!",fill="Red",font=("Times New Roman",45,"bold"))      
                else: 
                    mixer.init()
                    mixer.music.load("sounds/draw.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,700,text=f"The End, its Draw!!!",fill="Red",font=("Times New Roman",45,"bold"))    

            self.cont = 0
            self.startFlag=False            
            self.compFlag=True      



             

          

         
