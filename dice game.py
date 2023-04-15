import random
from tkinter import*
from PIL import ImageTk,Image
root=Tk()

root.title("endless dice game")
root.geometry("600x600")
root.configure(bg="yellow")

img=ImageTk.PhotoImage("dice.png")
player1_score=0
player2_score=0

player1=Label(root,bg="royal blue",fg="white",text="player1")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,bg="royal blue",fg="white",text="player2")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_score=Label(root,bg="red",fg="white")
player1_score.place(relx=0.1,rely=0.5,anchor=CENTER)

player2_score=Label(root,bg="red",fg="white")
player2_score.place(relx=0.9,rely=0.5,anchor=CENTER)

dice=Label(root,bg="#d33822",fg="#fa2435")
dice.place(relx=0.5,rely=0.5,anchor=CENTER)

def player_1():
    global player1_score
    r=random.randint(1, 6)
    player1["text"]="player1 dice no."+str(r)
    player1_score=player1_score+r














root.mainloop()