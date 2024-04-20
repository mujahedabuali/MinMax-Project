import customtkinter
from PIL import Image,ImageTk
from friendGUI import FriendGUI
from compEasyGUI import CompEasyGUI
from compHardGUI import CompHardGUI
from pygame import mixer

customtkinter.set_appearance_mode("Dark")

#Start page
class menuFrame(customtkinter.CTkFrame):
    def __init__(self, parent,easy,hard,freind):
        super().__init__(parent, corner_radius=0,fg_color="transparent")

        self.canvas = customtkinter.CTkCanvas(self, width=1600, height=900)
        self.canvas.pack(side="top",fill="both",expand=True)

        self.bgIMG = Image.open("icons/background.jpg").resize((1600, 900))
        self.bg_image = ImageTk.PhotoImage(self.bgIMG)
        self.canvas.create_image(0, 0, anchor=customtkinter.NW, image=self.bg_image)

        self.canvas.create_text(820,60,text="Tic Tac Toe.. ",fill="#2269a9",font=("Times New Roman",60,"italic"))
       
        self.iconIMG = Image.open("icons/tic-tac-toe.png").resize((250,250))
        self.icon_image = ImageTk.PhotoImage(self.iconIMG)
        self.canvas.create_image(680, 150, anchor=customtkinter.NW, image=self.icon_image)
        
        self.comp_image = customtkinter.CTkImage(Image.open("icons/desktop.png"),size=(30,30))
        self.friend_image = customtkinter.CTkImage(Image.open("icons/friendship.png"),size=(30,30))


        self.friendBttn = customtkinter.CTkButton( self.canvas,height=40,width=420,border_spacing=10, text="        Play with Friend", compound="left",image=self.friend_image,anchor="w",font=customtkinter.CTkFont(family="Times New Roman", size=30,weight="bold"),command=freind)
        self.friendBttn.place(x=600,y=480)

        self.compBttn = customtkinter.CTkButton( self.canvas, height=40,width=420,border_spacing=10, text=" Play with Computer 'Easy'", compound="left",image=self.comp_image, anchor="w",font=customtkinter.CTkFont(family="Times New Roman", size=30,weight="bold"),command=easy)
        self.compBttn.place(x=600,y=580)

        self.comp2Bttn = customtkinter.CTkButton( self.canvas, height=40,width=415,border_spacing=10, text=" Play with Computer 'Hard'", compound="left",image=self.comp_image, anchor="w",font=customtkinter.CTkFont(family="Times New Roman", size=30,weight="bold"),command=hard)
        self.comp2Bttn.place(x=600,y=660)


#Drive class
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("Dark")

        self.title("Tic Tac Toe")
        self.geometry("1600x900")
        center_x = int(150)
        center_y = int(70)
        self.geometry(f"+{center_x}+{center_y}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.freind=None
        self.easy=None
        self.hard=None
        
        self.mainPage=menuFrame(self,self.easyComp,self.hardComp,self.freindGame)
        self.mainPage.grid(row=0, column=1, sticky="nsew")


    def easyComp(self):
        self.select_frame_by_name("easy")

    def hardComp(self):
        self.select_frame_by_name("hard")    

    def freindGame(self):
        self.select_frame_by_name("freind")
    
    #to go a start page
    def main(self):
        self.select_frame_by_name("Menu") 

    #to move between page
    def select_frame_by_name(self, name):
         
        if self.freind != None:
             self.freind.destroy() 
        if self.easy != None:
             self.easy.destroy()       
        if self.hard != None:
             self.hard.destroy()            

        self.mainPage.grid_remove()
        mixer.init()
        mixer.music.load("sounds/click.wav")
        mixer.music.play()
        if name == "Menu":
            self.mainPage.grid(row=0, column=1, sticky="nsew")
        elif name == "freind":
            self.freind=FriendGUI(self,self.main)
            self.freind.grid(row=0, column=1, sticky="nsew")
        elif name == "easy":
            self.easy=CompEasyGUI(self,self.main)
            self.easy.grid(row=0, column=1, sticky="nsew")  
        elif name == "hard":
            self.hard=CompHardGUI(self,self.main)
            self.hard.grid(row=0, column=1, sticky="nsew")        

        self.update_idletasks()    
      
    
if __name__ == "__main__":
    app = App()
    app.mainloop()