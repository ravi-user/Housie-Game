from tkinter import *
from random import *
from tkinter import messagebox

screen = Tk()
screen.geometry("800x800")
screen.title('Housie')
screen.configure (bg='grey')

var = StringVar()
var1 = StringVar()
var2 = IntVar()

tickets = []
for i in range (18):
    n = randint(1,40)
    if n not in tickets:
        tickets.append(n)
player = set(sample(tickets, 6))
bot = set(sample(tickets, 6))
player=list(player)
bot=list(bot)

 


#----------
new_frame = Frame(screen,bg="grey",height=800,width=800, relief=RIDGE)
new_frame.place(x=0,y=0)
#@@@@@@@@@@@@
sec_frame = Frame(new_frame,bg="grey",height=800,width=800, relief=RIDGE)
sec_frame.place(x=0,y=0)
#------

def start():

    a=10
    b=400
    #----------
    sec_frame = Frame(new_frame,bg="grey",height=400,width=800, relief=RIDGE)
    sec_frame.place(x=0,y=0)
    #@@@@@@@@@@@@
    p = Label(sec_frame,textvariable=var,bg="grey",fg="black",font=('arial',18,'bold'))
    p.place(x = 30,y = 50)
    var.set("Player")

    p = Label(sec_frame,textvariable=var1,bg="grey",fg="black",font=('arial',18,'bold'))
    p.place(x = 500,y = 50)
    var1.set("Bot")

    for i in player:
        b1 = Button(sec_frame,text=i,bg="purple",fg="black",height=2,width=5,activebackground="blue")
        b1.place(x=a, y=150)
        a+=50

    for i in bot:
        b1 = Button(sec_frame,text=i,bg="yellow",fg="black",height=2,width=5,activebackground="blue")
        b1.place(x=b, y=150)
        b+=50



def Back():
    screen.destroy()

def Next():
    a = choice(tickets)
    var2.set(a)
    p = Label(new_frame,textvariable=var2,bg="grey",fg="white",font=('arial',18,'bold'))
    p.place(x = 300,y = 400)
     
    if a in player:
        player.remove(a)    
    if a in bot:
        bot.remove(a)
    tickets.remove(a)
    sec_frame.destroy
    start()
    
    if len(player)==0 and len(bot)==0:
        win = Label(new_frame,text="Match Draw",bg="orange",fg="white",font=('arial',15,'bold'))
        win.place(x=250,y=600)
        box=messagebox.askokcancel(title="Game Over!", message="Match Draw", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
        
    elif len(player)==0:
        win = Label(new_frame,text="Winner is Player",bg="orange",fg="white",font=('arial',15,'bold'))
        win.place(x=250,y=600)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player1 win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
            
    elif len(bot)==0:
        win = Label(new_frame,text="Winner is Bot",bg="orange",fg="white",font=('arial',15,'bold'))
        win.place(x=250,y=600)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player2 win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home

#---  

start()

b1 = Button(new_frame,text="Next",bg="black",fg="white",height=3,width=8,font=('arial',12,'bold'),activebackground="green",command=Next)
b1.place(x = 180,y = 450)

b1 = Button(new_frame,text="Quit",bg="black",fg="white",height=3,width=8,font=('arial',12,'bold'),activebackground="red",command=Back)
b1.place(x = 330,y = 450)

def disabled():
    b1["state"]=="DISABLED"

screen.mainloop()



