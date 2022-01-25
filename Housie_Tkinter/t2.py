from frame import *
from tkinter import *
from random import *

screen = Tk()
screen.geometry("700x700")
screen.title('Housie')

tickets=[]

for i in range(18):
    n=randint(1,40)
    if n not in tickets:
        tickets.append(n)

print(tickets)

player1 = set(sample(tickets,6))
player2 = set(sample(tickets,6))

player1=list(player1)
player2=list(player2)

print(player1)
print(player2)


b1 = Button(screen,text="Next",bg="white",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Next)
b1.place(x = 180,y = 450)

b1 = Button(screen,text="Quit",bg="white",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Back)
b1.place(x = 330,y = 450)

p = Label(new_frame,textvariable=var,bg="blue",fg="white",font=('arial',18,'bold'))
p.place(x = 30,y = 30)
var.set("Player")

p = Label(new_frame,textvariable=var1,bg="blue",fg="white",font=('arial',18,'bold'))
p.place(x = 500,y = 30)
var1.set("Bot")


screen.mainloop()