from tkinter import *
from random import *
from tkinter import messagebox

screen = Tk()
screen.geometry("800x800")
screen.title('Housie')
screen.configure(bg='grey')

var = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = IntVar()

tickets = []
for i in range (24):
    n = randint(1,40)
    if n not in tickets:
        tickets.append(n)
player1 = set(sample(tickets, 6))
player2 = set(sample(tickets, 6))
player3 = set(sample(tickets, 6))
player4 = set(sample(tickets, 6))

player1 = list(player1)
player2 = list(player2)
player3 = list(player3)
player4 = list(player4)

def Back():
    screen.destroy()

         

#----------
new_frame = Frame(screen,bg="grey",height=800,width=800, relief=RIDGE)
new_frame.place(x=0,y=0)
#@@@@@@@@@@@@
sec_frame = Frame(new_frame,bg="grey",height=500,width=800, relief=RIDGE)
sec_frame.place(x=0,y=0)
#------

#---
def start():
    a=10
    b=450
    c=10
    d=450
    #------
    sec_frame = Frame(new_frame,bg="grey",height=500,width=800, relief=RIDGE)
    sec_frame.place(x=0,y=0)

    p = Label(sec_frame,textvariable=var,bg="grey",fg="black",font=('arial',18,'bold'))
    p.place(x=30,y=30)
    var.set("Player1")

    p = Label(sec_frame,textvariable=var2,bg="grey",fg="black",font=('arial',18,'bold'))
    p.place(x=500,y=30)
    var2.set("Player2")

    p1 = Label(sec_frame,textvariable=var3,bg="grey",fg="black",font=('arial',18,'bold'))
    p1.place(x=30,y=300)
    var3.set("Player3")

    p1 = Label(sec_frame,textvariable=var4,bg="grey",fg="black",font=('arial',18,'bold'))
    p1.place(x=500,y=300)
    var4.set("Player4")
    for i in player1:
        b1 = Button(sec_frame,text=i,bg="purple",fg="black",height=2,width=5)
        b1.place(x=a, y=150)
        a+=50

    for i in player2:
        b1 = Button(sec_frame,text=i,bg="pink",fg="black",height=2,width=5)
        b1.place(x=b, y=150)
        b+=50
        
    for i in player3:
        b1 = Button(sec_frame,text=i,bg="purple",fg="black",height=2,width=5)
        b1.place(x=c,y=400)
        c+=50

    for i in player4:
        b1 = Button(sec_frame,text=i,bg="pink",fg="black",height=2,width=5)
        b1.place(x=d, y=400)
        d+=50
#--------

def Next():
    a = choice(tickets)
    var5.set(a)
    p = Label(screen,textvariable=var5,bg="grey",fg="white",font=('arial',18,'bold'))
    p.place(x = 350,y = 500)
     
    if a in player1:
        player1.remove(a)    
    if a in player2:
        player2.remove(a)
    if a in player3:
        player3.remove(a)
    if a in player4:
        player4.remove(a)    
    tickets.remove(a)
    sec_frame.destroy
    start()

    
    if (len(player1)==0 and len(player2)==0) or (len(player2)==0 and len(player3)==0) or (len(player3)==0 and len(player4)==0) or (len(player1)==0 and len(player4)==0):
        win = Label(new_frame,text="Match Draw",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Match Draw", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
    elif len(player1)==0:
        win = Label(new_frame,text="Winner is Player1",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player1 win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
    elif len(player2)==0:
        win = Label(new_frame,text="Winner is Player2",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player2  win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
    elif len(player3)==0:
        win = Label(new_frame,text="Winner is Player3",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player3  win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
    elif len(player4)==0:
        win = Label(new_frame,text="Winner is Player4",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player4  win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home

#----            
start()
b1 = Button(new_frame,text="Next",bg="black",fg="white",height=3,width=8,font=('arial',12,'bold'),activebackground="green",command=Next)
b1.place(x = 250,y = 570)

b1 = Button(new_frame,text="Quit",bg="black",fg="white",height=3,width=8,font=('arial',12,'bold'),activebackground="red",command=Back)
b1.place(x = 400,y = 570)
 

screen.mainloop()