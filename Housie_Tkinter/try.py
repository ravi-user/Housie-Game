from tkinter import *
from random import *

screen = Tk()
screen.geometry("800x600")
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



a=10
b=400
#------
for i in player:
    b1 = Button(screen,text=i,bg="white",fg="black",height=2,width=5,activebackground="blue")
    b1.place(x=a, y=100)
    a+=50
    print(player)

for i in bot:
    b1 = Button(screen,text=i,bg="white",fg="black",height=2,width=5,activebackground="blue")
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
    # for i in player:
    #     i=a
    #     if a in player:
    #         player.remove(a)    
    # if a in bot:
    #     bot.remove(a)
    # tickets.remove(a)
    
     
    #print(f"\n  __Ticket is {x}__")
     
    if a in player:
        player.remove(a)    
    if a in bot:
        bot.remove(a)
    tickets.remove(a)
 



b1 = Button(screen,text="Next",bg="white",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Next)
b1.place(x = 180,y = 450)

b1 = Button(screen,text="Quit",bg="white",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Back)
b1.place(x = 330,y = 450)

p = Label(screen,textvariable=var,bg="blue",fg="white",font=('arial',18,'bold'))
p.place(x = 30,y = 30)
var.set("Player")

p = Label(screen,textvariable=var1,bg="blue",fg="white",font=('arial',18,'bold'))
p.place(x = 500,y = 30)
var1.set("Bot")

# p = Label(screen,textvariable=var2,bg="blue",fg="white",font=('arial',18,'bold'))
# p.place(x = 300,y = 400)
 

# pl1 = Button(screen,text=p ,bg="white",fg="black",font=('arial',10,'bold'))
# pl1.place(x=30 , y=70)

screen.mainloop()