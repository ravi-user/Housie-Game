from tkinter import *
from random import *

screen = Tk()
screen.geometry("800x700")
screen.title('Housie')
screen.configure (bg='blue')

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
print(player)
 


#----------
new_frame = Frame(screen,bg="blue",height=400,width=800, relief=RIDGE)
new_frame.pack(side=TOP)
#@@@@@@@@@@@@
sec_frame = Frame(new_frame,bg="blue",height=400,width=800, relief=RIDGE)
sec_frame.place(x=0,y=0)
#------
def start():

    a=10
    b=400
    #----------
    sec_frame = Frame(new_frame,bg="blue",height=400,width=800, relief=RIDGE)
    sec_frame.place(x=0,y=0)
    #@@@@@@@@@@@@
    p = Label(sec_frame,textvariable=var,bg="blue",fg="white",font=('arial',18,'bold'))
    p.place(x = 30,y = 30)
    var.set("Player")

    p = Label(sec_frame,textvariable=var1,bg="blue",fg="white",font=('arial',18,'bold'))
    p.place(x = 500,y = 30)
    var1.set("Bot")

    for i in player:
        b1 = Button(sec_frame,text=i,bg="white",fg="black",height=2,width=5,activebackground="blue")
        b1.place(x=a, y=100)
        a+=50
        print(player)

    for i in bot:
        b1 = Button(sec_frame,text=i,bg="white",fg="black",height=2,width=5,activebackground="blue")
        b1.place(x=b, y=100)
        b+=50
        print(bot)


def Back():
    screen.destroy()

def Next():
    a = choice(tickets)
    var2.set(a)
    p = Label(screen,textvariable=var2,bg="blue",fg="white",font=('arial',18,'bold'))
    p.place(x = 300,y = 400)
     
    if a in player:
        player.remove(a)    
    if a in bot:
        bot.remove(a)
    tickets.remove(a)
    sec_frame.destroy
    start()
    
    if len(player)==0 and len(bot)==0:
        win = Label(screen,text="Match Draw",bg="white",fg="black",font=('arial',15,'bold'))
        win.place(x=250,y=600)
        disabled()
        
    elif len(player)==0:
        win = Label(screen,text="Winner is Player",bg="white",fg="black",font=('arial',15,'bold'))
        win.place(x=250,y=600)
        disabled()
            
    elif len(bot)==0:
        win = Label(screen,text="Winner is Bot",bg="white",fg="black",font=('arial',15,'bold'))
        win.place(x=250,y=600)
        disabled()

#---  

start()

b1 = Button(screen,text="Next",bg="white",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Next)
b1.place(x = 180,y = 450)

b1 = Button(screen,text="Quit",bg="white",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Back)
b1.place(x = 330,y = 450)

def disabled():
    b1["state"]=="DISABLED"

screen.mainloop()



