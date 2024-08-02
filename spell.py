import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("spell checker")
root.geometry("700x500")
#root.config(background="maroon")

def check():
    word=textfield.get()
    c=TextBlob(word)
    right=str(c.correct())
    spell.config(text=right) 

cs=Label(root,text="Correct Spelling :",font=("poppins",15,"bold"),fg="black")
cs.place(x=100,y=300)

heading=Label(root, text="spelling checker", font=("Arial", 30, "bold"), fg="green")
heading.pack()

textfield=Entry(root,justify="center",width=30,font=("poppins",25),border=2)
textfield.pack(pady=40)
textfield.focus()

button=Button(root,text="check",font=("times new roman",20,"bold"),fg="black",bg="skyblue",command=check)
button.pack()

spell=Label(root,font=("poppins",15))
spell.place(x=350,y=300)

root.mainloop()