from tkinter import *

screen = Tk()
screen.geometry("800x800")
screen.title('Housie')
screen.configure(bg='grey')
var = StringVar()
var1 = StringVar()

def Stop():
    screen.destroy()

def Start():
    screen.destroy()
    import Player_Selection

b1 = Button(screen,text="Start",bg="purple",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="green",command=Start)
b1.place(x = 180,y = 300)


b1 = Button(screen,text="Quit",bg="purple",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="red",command=Stop)
b1.place(x = 330,y = 300)

l1 = Label(screen,textvariable=var,bg="grey",fg="white",font=('arial',30,'bold'))
l1.place(x = 135,y = 150)
l2 = Label(screen,textvariable=var1,bg="grey",fg="white",font=('arial',30,'bold'))
l2.place(x = 320,y = 150)
var.set("Welcome")
var1.set("To Housie")

screen.mainloop()
 