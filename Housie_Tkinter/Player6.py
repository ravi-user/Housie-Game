from tkinter import *
from random import *
from tkinter import messagebox

screen = Tk()
screen.geometry("800x800")
screen.title('Housie')
screen.configure (bg='grey')

var = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()


tickets = []
for i in range (36):
    n = randint(1,40)
    if n not in tickets:
        tickets.append(n)
player1 = set(sample(tickets, 6))
player2 = set(sample(tickets, 6))
player3 = set(sample(tickets, 6))
player4 = set(sample(tickets, 6))
player5 = set(sample(tickets, 6))
player6 = set(sample(tickets, 6))

player1 = list(player1)
player2 = list(player2)
player3 = list(player3)
player4 = list(player4)
player5 = list(player5)
player6 = list(player6)

#----------
new_frame = Frame(screen,bg="grey",height=800,width=800, relief=RIDGE)
new_frame.place(x=0,y=0)
#@@@@@@@@@@@@
sec_frame = Frame(new_frame,bg="grey",height=500,width=800, relief=RIDGE)
sec_frame.place(x=0,y=0)
#------

def Back():
    screen.destroy()

#---
def start():
    a=30
    b=460
    c=30
    d=460
    e=30
    f=460
    #------
    sec_frame = Frame(new_frame,bg="grey",height=500,width=800, relief=RIDGE)
    sec_frame.place(x=0,y=0)

    p = Label(sec_frame,textvariable=var,bg="grey",fg="black",font=('arial',18,'bold'))
    p.place(x=120,y=30)
    var.set("Player1")

    p = Label(sec_frame,textvariable=var2,bg="grey",fg="black",font=('arial',18,'bold'))
    p.place(x=570,y=30)
    var2.set("Player2")

    p1 = Label(sec_frame,textvariable=var3,bg="grey",fg="black",font=('arial',18,'bold'))
    p1.place(x=120,y=180)
    var3.set("Player3")

    p1 = Label(sec_frame,textvariable=var4,bg="grey",fg="black",font=('arial',18,'bold'))
    p1.place(x=570,y=180)
    var4.set("Player4")

    p1 = Label(sec_frame,textvariable=var6,bg="grey",fg="black",font=('arial',18,'bold'))
    p1.place(x=120,y=330)
    var6.set("Player5")

    p1 = Label(sec_frame,textvariable=var7,bg="grey",fg="black",font=('arial',18,'bold'))
    p1.place(x=570,y=330)
    var7.set("Player6")

    for i in player1:
        b1 = Button(sec_frame,text=i,bg="purple",fg="black",height=2,width=5)
        b1.place(x=a, y=100)
        a+=50

    for i in player2:
        b1 = Button(sec_frame,text=i,bg="pink",fg="black",height=2,width=5)
        b1.place(x=b, y=100)
        b+=50
        
    for i in player3:
        b1 = Button(sec_frame,text=i,bg="purple",fg="black",height=2,width=5)
        b1.place(x=c,y=250)
        c+=50

    for i in player4:
        b1 = Button(sec_frame,text=i,bg="pink",fg="black",height=2,width=5)
        b1.place(x=d, y=250)
        d+=50

    for i in player5:
        b1 = Button(sec_frame,text=i,bg="purple",fg="black",height=2,width=5)
        b1.place(x=e,y=400)
        e+=50

    for i in player6:
        b1 = Button(sec_frame,text=i,bg="pink",fg="black",height=2,width=5)
        b1.place(x=f, y=400)
        f+=50

def Next():
    a = choice(tickets)
    var5.set(a)
    p = Label(new_frame,textvariable=var5,bg="grey",fg="white",font=('arial',18,'bold'))
    p.place(x = 360,y = 500)

    if a in player1:
        player1.remove(a)
    if a in player2:
        player2.remove(a)
    if a in player3:
        player3.remove(a)
    if a in player4:
        player4.remove(a)
    if a in player5:
        player5.remove(a)
    if a in player6:
        player6.remove(a)
    
    sec_frame.destroy
    start()

    if (len(player1)==0 and len(player2)==0) or (len(player2)==0 and len(player3)==0) or (len(player3)==0 and len(player4)==0) or (len(player4)==0 and len(player5)==0) or (len(player5)==0 and len(player6)==0) or (len(player1)==0 and len(player6)==0):
        win = Label(new_frame,text="Match Draw",bg="orange",fg="white",font=('arial',15,'bold'))
        win.place(x=250,y=600)
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
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player2 win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
    elif len(player3)==0:
        win = Label(new_frame,text="Winner is Player3",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player3 win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
    elif len(player4)==0:
        win = Label(new_frame,text="Winner is Player4",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player4 win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
    elif len(player5)==0:
        win = Label(new_frame,text="Winner is Player4",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player5 win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home
    elif len(player6)==0:
        win = Label(new_frame,text="Winner is Player6",bg="orange",fg="white",font=('arial',20,'bold'))
        win.place(x=250,y=700)
        box=messagebox.askokcancel(title="Game Over!", message="Congratulations.. Player1 win", default=messagebox.OK)
        if box:
            screen.destroy()
            import Home


#---
start()

b1 = Button(new_frame,text="Next",bg="black",fg="white",height=3,width=8,font=('arial',12,'bold'),activebackground="green",command=Next)
b1.place(x = 250,y = 550)

b1 = Button(new_frame,text="Quit",bg="black",fg="white",height=3,width=8,font=('arial',12,'bold'),activebackground="green",command=Back)
b1.place(x = 400,y = 550)

screen.mainloop()