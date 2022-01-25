from tkinter import *

screen = Tk()
screen.geometry("800x800")
screen.title('Housie')
screen.configure (bg='grey')
    
def Player2():
    screen.destroy()
    import Player2

def Player4():
    screen.destroy()
    import Player4

def Player6():
    screen.destroy()
    import Player6

b1 = Button(screen,text="2 Players",bg="purple",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Player2)
b1.place(x = 150,y = 300)


b1 = Button(screen,text="4 Players",bg="purple",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Player4)
b1.place(x = 300,y = 300)

b1 = Button(screen,text="6 Players",bg="purple",fg="black",height=3,width=8,font=('arial',12,'bold'),activebackground="blue",command=Player6)
b1.place(x = 450,y = 300)

l1 = Label(screen,text="Select Players",bg="green",fg="white",font=('arial',25,'bold'))
l1.place(x=200,y=200)

screen.mainloop()