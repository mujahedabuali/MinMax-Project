import customtkinter as customtkinter
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from pygame import mixer
from PIL import Image,ImageTk
from player import Player

customtkinter.set_appearance_mode('dark')

class FriendGUI(customtkinter.CTkFrame):
    def __init__(self, parent,main):
        super().__init__(parent, corner_radius=0)

        self.canvas = customtkinter.CTkCanvas(self, width=1600, height=900)
        self.canvas.pack(side="top",fill="both",expand=True)

        #images
        self.bgIMG = Image.open("icons/background.jpg").resize((1600, 900))
        self.bg_image = ImageTk.PhotoImage(self.bgIMG)
        self.o_image = Image.open("icons/O.png").resize((70, 70))
        self.o_image = ImageTk.PhotoImage(self.o_image)
        self.x_image = Image.open("icons/clear.png").resize((70, 70))
        self.x_image = ImageTk.PhotoImage(self.x_image)

        self.canvas.create_image(0, 0, anchor=customtkinter.NW, image=self.bg_image)
    
        self.canvas.create_text(800,60,text="Tic Tac Toe ..",fill="#2269a9",font=("Times New Roman",45,"italic"))
        
        self.canvas.create_text(190,80,text="Current Turn : ",fill="white",font=("Times New Roman",29,"italic"))
        self.turnName=self.canvas.create_text(350,80,text="",fill="#4ac374",font=("Times New Roman",34,"italic"))


        self.canvas.create_text(190,350,text="SCORE",fill="white",font=("Times New Roman",34,"italic"))
        
        self.playerName1=self.canvas.create_text(190,430,text="You :",fill="#4ac374",font=("Times New Roman",34,"italic"))
        self.res1=self.canvas.create_text(290,430,text="0",fill="White",font=("Times New Roman",34,"italic"))
        
        self.playerName2=self.canvas.create_text(190,480,text="Opponent :",fill="red",font=("Times New Roman",32,"italic"))
        self.res2=self.canvas.create_text(290,480,text="0",fill="White",font=("Times New Roman",34,"italic"))
        
        self.curRoundLabel=self.canvas.create_text(175,560,text="1",fill="white",font=("Times New Roman",34,"italic"))
        self.MaxRoundLabel=self.canvas.create_text(195,560,text="/1",fill="white",font=("Times New Roman",34,"italic"))
        self.curRound=1
        self.MaxRound=0

        self.canvas.create_text(1250,80,text="Choose X or ... ",fill="white",font=("Times New Roman",32,"italic"))
        
        self.x_o=customtkinter.StringVar()
        self.x_o.set("O")
        self.option=customtkinter.CTkOptionMenu(self.canvas, values=["O","X"],variable=self.x_o)
        self.option.place(x=1350,y=70)

        self.startBttn= customtkinter.CTkButton(self.canvas,text="Start Game",width=160,height=35,command=self.start)
        self.restBttn= customtkinter.CTkButton(self.canvas,text="Reset Game",width=160,height=35,command=self.reset)
        self.backBttn= customtkinter.CTkButton(self.canvas,text="Back to Main",width=160,height=35,fg_color="red",command=main)

        self.startBttn.place(x=1220,y=320)
        self.restBttn.place(x=1220,y=390)
        self.backBttn.place(x=1220,y=470)


        # Draw horizontal lines
        board_x = 635
        board_y = 340
        cell_size = 100
        for i in range(1, 3):
            self.canvas.create_line(board_x, board_y + i * cell_size, board_x + 3 * cell_size, board_y + i * cell_size, width=5,fill="#990000")

        # Draw vertical lines
        for i in range(1, 3):
            self.canvas.create_line(board_x + i * cell_size, board_y, board_x + i * cell_size, board_y + 3 * cell_size, width=5,fill="#990000")
        
        self.player1 = Player("","")
        self.player2 = Player("","")
        self.answeX=[]
        self.answeO=[]
     

        self.play()
        self.windowName()
    

    #make Boxes
    def play(self):   

        #flags and global veriable
        self.startFlag=False
        self.compFlag=False
        self.compChoose_Label = None
        self.buttons = [[None, None, None] for _ in range(3)]
        self.answeX=[]
        self.answeO=[]
        self.option.configure(state="normal")
        self.resLabel = None
        self.board = [[0, 0, 0] for _ in range(3)]

        

        self.button1= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(1,635,343))
        self.buttons[0][0]=(self.button1)
        self.button1.place(x=640,y=343)
        self.button2= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(2,735,343))
        self.buttons[0][1]=(self.button2)
        self.button2.place(x=740,y=343)
        self.button3= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(3,835,343))
        self.button3.place(x=840,y=343)
        self.buttons[0][2]=(self.button3)
        self.button4= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(4,635,443))
        self.button4.place(x=640,y=443)
        self.buttons[1][0]=(self.button4)
        self.button5= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(5,735,443))
        self.button5.place(x=740,y=443)
        self.buttons[1][1]=(self.button5)
        self.button6= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(6,835,443))
        self.button6.place(x=840,y=443)
        self.buttons[1][2]=(self.button6)
        self.button7= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(7,635,543))
        self.button7.place(x=640,y=543)
        self.buttons[2][0]=(self.button7)
        self.button8= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(8,735,543))
        self.button8.place(x=740,y=543)
        self.buttons[2][1]=(self.button8)
        self.button9= tk.Button(self.canvas, text="",width=8,height=6,font=("Helvetica",12),command=lambda:self.press(9,835,543))
        self.button9.place(x=840,y=543)
        self.buttons[2][2]=(self.button9)


    #to display a names window
    def windowName(self):
        self.bgIMG2 = Image.open("icons/background.jpg").resize((450, 400))
        self.bg_image2 = ImageTk.PhotoImage(self.bgIMG2)
        namesWindow =customtkinter.CTkToplevel(self)
        namesWindow.title("Players Name")
        namesWindow.geometry("450x400")
        namesWindow.resizable(False, False)
        def do_nothing():
         pass
        namesWindow.protocol("WM_DELETE_WINDOW", do_nothing)

        center_x = int(700)
        center_y = int(350)
        namesWindow.geometry(f"+{center_x}+{center_y}")

        canvas = customtkinter.CTkCanvas(namesWindow, width=450, height=400)
        canvas.pack(side="top",fill="both",expand=True)
        canvas.create_image(0, 0, anchor=customtkinter.NW, image=self.bg_image2)
        
        self.IMG1 = Image.open("icons/athlete.png").resize((35, 35))
        self.player1_image = ImageTk.PhotoImage(self.IMG1)
        canvas.create_image(80, 15, anchor=customtkinter.NW, image=self.player1_image)

        canvas.create_text(250,35,text="Name of Player one: ",fill="White",font=("Times New Roman",30,"italic"))
        
        entry = customtkinter.CTkEntry(canvas)
        entry.delete(0, customtkinter.END)
        entry.insert(0, "Player 1")
        entry.place(x=160,y=75)

        self.IMG2 = Image.open("icons/soccer-player.png").resize((35, 35))
        self.player2_image = ImageTk.PhotoImage(self.IMG2)
        canvas.create_image(80, 130, anchor=customtkinter.NW, image=self.player2_image)

        canvas.create_text(250,150,text="Name of Player two:",fill="White",font=("Times New Roman",30,"italic"))

        entry2 = customtkinter.CTkEntry(canvas)
        entry2.delete(0, customtkinter.END)
        entry2.insert(0, "Player 2")
        entry2.place(x=160,y=200)

        canvas.create_text(160,280,text="Rounds:",fill="White",font=("Times New Roman",28,"italic"))
        num_round = customtkinter.StringVar()
        combobox = customtkinter.CTkComboBox(master=canvas,width=5,variable=num_round,values=["1", "2", "3", "4", "5"])
        num_round.set("1")
        combobox.place(x=240,y=270)


        def names():
            mixer.init()
            mixer.music.load("sounds/click.wav")
            mixer.music.play()
            if entry2.get() != "" and entry.get() !="":
                self.canvas.itemconfig(self.playerName1, text=f"{entry.get()} :")
                self.canvas.itemconfig(self.playerName2, text=f"{entry2.get()} :")
                self.canvas.itemconfig(self.MaxRoundLabel,text=f"/{num_round.get()}")
                self.MaxRound=num_round.get()
                namesWindow.destroy()

        submit_button = customtkinter.CTkButton(canvas, text="Done",command=names)
        submit_button.place(x=160,y=350)   

    #for start button
    def start(self):
        mixer.init()
        mixer.music.load("sounds/start.wav")
        mixer.music.play()
        
        self.startFlag =True
        self.cont =0
        self.board = [[0, 0, 0] for _ in range(3)]
        self.option.configure(state="disabled")
        
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
            if name1 == name1Split[0] :
                self.player1.name=name1
                self.player2.name=name2
                self.canvas.itemconfig(self.turnName, text=f"{self.player1.name}")
                self.canvas.itemconfig(self.turnName, fill=f"{color}")
                self.player1.icon=self.x_o.get()

                if self.x_o.get() =="X":
                    self.player2.icon="O"
                else :  self.player2.icon="X" 
            else:    
                self.player1.name=name2
                self.player2.name=name1
                self.canvas.itemconfig(self.turnName, text=f"{self.player2.name}")
                self.canvas.itemconfig(self.turnName, fill=f"{color}")
                self.player2.icon=self.x_o.get()

                if self.x_o.get() =="X":
                    self.player1.icon="O"
                else :  self.player1.icon="X" 


            for i in self.answeO:
                self.canvas.delete(i)
            for ii in self.answeX:
                self.canvas.delete(ii)
                
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


    def press(self,num,x,y):
        if self.startFlag == True:
            mixer.init()
            mixer.music.load("sounds/buttonclick.wav")
            mixer.music.play()
            self.startBttn.configure(state="disabled")

            if  self.state=="X" :
                self.answeX.append(self.canvas.create_image(x+10, y+10, anchor=customtkinter.NW, image=self.x_image))
                if num == 1:
                    self.board[0][0]=-1;
                    self.button1.destroy()
                elif num == 2:
                    self.board[0][1]=-1;
                    self.button2.destroy()
                elif num == 3:
                    self.board[0][2]=-1;
                    self.button3.destroy()
                elif num == 4:
                    self.board[1][0]=-1;
                    self.button4.destroy()
                elif num == 5:
                    self.board[1][1]=-1;
                    self.button5.destroy()
                elif num == 6:
                    self.board[1][2]=-1;
                    self.button6.destroy()
                elif num == 7:
                    self.board[2][0]=-1;
                    self.button7.destroy()
                elif num == 8:
                    self.board[2][1]=-1;
                    self.button8.destroy()
                else:
                    self.board[2][2]=-1;
                    self.button9.destroy()
                
                self.cont += 1
                self.state="O"

                if self.player1.icon=="X":
                    self.canvas.itemconfig(self.turnName, text=f"{self.player2.name}")
                else :    self.canvas.itemconfig(self.turnName, text=f"{self.player1.name}")

                self.checkWin()
            else:
                self.answeO.append(self.canvas.create_image(x+10, y+10, anchor=customtkinter.NW, image=self.o_image))
                if num == 1:
                    self.board[0][0]=1;
                    self.button1.destroy()
                elif num == 2:
                    self.board[0][1]=1;
                    self.button2.destroy()
                elif num == 3:
                    self.board[0][2]=1;
                    self.button3.destroy()
                elif num == 4:
                    self.board[1][0]=1;
                    self.button4.destroy()
                elif num == 5:
                    self.board[1][1]=1;
                    self.button5.destroy()
                elif num == 6:
                    self.board[1][2]=1;
                    self.button6.destroy()
                elif num == 7:
                    self.board[2][0]=1;
                    self.button7.destroy()
                elif num == 8:
                    self.board[2][1]=1;
                    self.button8.destroy()
                else:
                    self.board[2][2]=1;
                    self.button9.destroy()
                
                self.cont += 1
                self.state="X"

                if self.player1.icon=="O":
                    self.canvas.itemconfig(self.turnName, text=f"{self.player2.name}")
                else :self.canvas.itemconfig(self.turnName, text=f"{self.player1.name}")

                self.checkWin()

    #check if ended
    def checkWin(self):
        x=self.board_state(self.board)
        
        if(x==-1):
            mixer.init()
            mixer.music.load("sounds/win.wav")
            mixer.music.play()
            if self.player1.icon == "X":
                self.resLabel=self.canvas.create_text(790,715,text=f"{self.player1.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))
                self.player1.points+=1
                self.canvas.itemconfig(self.res1, text=f"{self.player1.points}")
            else: 
                self.resLabel=self.canvas.create_text(790,715,text=f"{self.player2.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))  
                self.player2.points+=1 
                self.canvas.itemconfig(self.res2, text=f"{self.player2.points}")
                
            
            if(int(self.curRound)<int(self.MaxRound)):
                self.nexBttn =customtkinter.CTkButton(self.canvas,text="Next Round!",width=160,height=35,command=self.nextRound) 
                self.nexBttn.place(x=730,y=780)
            else:
                if self.player1.points>self.player2.points :
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, {self.player1.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))  
                elif self.player1.points<self.player2.points:
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, {self.player2.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))      
                else:
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, its Draw!!!",fill="Red",font=("Times New Roman",40,"bold")) 
            
            self.cont = 0
            self.compFlag=True
            self.startFlag=False           
         

        if(x==1):
            mixer.init()
            mixer.music.load("sounds/win.wav")
            mixer.music.play()
            if self.player1.icon == "O":
                self.resLabel=self.canvas.create_text(790,715,text=f"{self.player1.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))
                self.player1.points+=1
                self.canvas.itemconfig(self.res1, text=f"{self.player1.points}")
            else: 
                self.resLabel=self.canvas.create_text(790,715,text=f"{self.player2.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))  
                self.player2.points+=1 
                self.canvas.itemconfig(self.res2, text=f"{self.player2.points}")


            if(int(self.curRound)<int(self.MaxRound)):
                self.nexBttn =customtkinter.CTkButton(self.canvas,text="Next Round!",width=160,height=35,command=self.nextRound) 
                self.nexBttn.place(x=730,y=780)
            else:
                if self.player1.points>self.player2.points :
                    mixer.init()
                    mixer.music.load("sounds/win.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, {self.player1.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))  
                elif self.player1.points<self.player2.points:
                    mixer.init()
                    mixer.music.load("sounds/win.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, {self.player2.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))      
                else:
                    mixer.init()
                    mixer.music.load("sounds/draw.wav")
                    mixer.music.play()
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, its Draw!!!",fill="Red",font=("Times New Roman",40,"bold"))    
            
            self.compFlag=True
            self.startFlag=False
            self.cont = 0

        elif (self.cont == 9):
            self.resLabel=self.canvas.create_text(790,715,text="DRAW!!!",fill="Red",font=("Times New Roman",40,"bold"))

            if(int(self.curRound)<int(self.MaxRound)):
                self.nexBttn =customtkinter.CTkButton(self.canvas,text="Next Round!",width=160,height=35,command=self.nextRound) 
                self.nexBttn.place(x=730,y=780)
            else :
                if self.player1.points>self.player2.points :
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, {self.player1.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))  
                elif self.player1.points<self.player2.points:  
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, {self.player2.name} Win!!!",fill="Red",font=("Times New Roman",40,"bold"))      
                else: 
                    self.canvas.delete(self.resLabel) 
                    self.resLabel=self.canvas.create_text(790,715,text=f"The End, its Draw!!!",fill="Red",font=("Times New Roman",40,"bold"))    

            self.cont = 0
            self.startFlag=False            
            self.compFlag=True

     #This function is used to analyze a game.
    def board_state(self,board):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] == -1 )or \
               (self.board[0][i] == self.board[1][i] == self.board[2][i] == -1):
                
                return -1
        
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] == 1 )or \
               (self.board[0][i] == self.board[1][i] == self.board[2][i] == 1):
                
                return 1    

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == -1 or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == -1:
            
            return -1 
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 1 or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == 1:
            
            return 1      
        
        else : return 0
       
            
    #for clear before next rounf
    def clear(self):
        for i in self.answeO:
            self.canvas.delete(i)
        for i in self.answeX:
            self.canvas.delete(i) 

        for row in self.buttons:
            for button in row:
                button.destroy()
                    
        if self.resLabel != None:
            self.canvas.delete(self.resLabel)
            self.resLabel = None

        if self.compChoose_Label != None:
                    self.canvas.delete(self.compChoose_Label)
                    self.compChoose_Label = None    

        self.startBttn.configure(state="normal")
        self.compFlag=False    
        self.board = [[0, 0, 0] for _ in range(3)]
        self.play()

    #nexRound
    def nextRound(self):
        mixer.init()
        mixer.music.load("sounds/click.wav")
        mixer.music.play()
        self.curRound+=1
        self.canvas.itemconfig(self.curRoundLabel, text=f"{self.curRound}")
        self.nexBttn.destroy()
        self.clear()
        self.start()

    #reset and start from begine
    def reset(self):
        mixer.init()
        mixer.music.load("sounds/click.wav")
        mixer.music.play()
        self.curRound=1
        self.player1.points=0
        self.player2.points=0
        self.canvas.itemconfig(self.curRoundLabel, text=f"{self.curRound}")
        self.canvas.itemconfig(self.res1, text=f"0")
        self.canvas.itemconfig(self.res2, text=f"0")
        self.canvas.itemconfig(self.turnName, text=f"")
        self.clear()
        self.windowName()

        



            
         








     


   