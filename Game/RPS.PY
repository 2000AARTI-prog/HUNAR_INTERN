from tkinter import *
from PIL import Image,ImageTk
from random import randint

# main window.............
root = Tk()
root.title("ROCK PAPER SCCISSOR")
root.configure(background="black")

# picture..............
rock_img=ImageTk.PhotoImage(Image.open("user_rock.jpg"))
paper_img=ImageTk.PhotoImage(Image.open("user_paper.jpg"))
scissor_img=ImageTk.PhotoImage(Image.open("user_scissor.jpg"))
cmp_rock_img=ImageTk.PhotoImage(Image.open("cmp_rock.jpg"))
cmp_paper_img=ImageTk.PhotoImage(Image.open("cmp_paper.jpg"))
cmp_scissor_img=ImageTk.PhotoImage(Image.open("cmp_scissor.jpg"))

# insert picture............
user_label=Label(root,image=paper_img,bg="black")
comp_label=Label(root,image=cmp_paper_img,bg="black")
user_label.grid(row=4,column=2)
comp_label.grid(row=3,column=2)

# scores...............
playerscore=Label(root,text=0,font=50,bg="black",fg="orange")
computerscore=Label(root,text=0,font=50,bg="black",fg="orange")
playerscore.grid(row=5,column=3)
computerscore.grid(row=2,column=3)

# indicators..............
user_indicator=Label(root,font=50,text="Player",bg="black",fg="purple")
comp_indicator=Label(root,font=50,text="Computer",bg="black",fg="purple",)
user_indicator.grid(row=5,column=1)
comp_indicator.grid(row=2,column=1)

# message...............
msg=Label(root,font=50,bg="black",fg="orange")
msg.grid(row=1,column=2)

# update message..............
def updateMessage(x):
    msg['text']=x

# update user score.............
def updateUserScore():
    score=int(playerscore["text"])
    score+=1
    playerscore["text"]=str(score)

# update computer score.............
def updateCompScore():
    score=int(computerscore["text"])
    score+=1
    computerscore["text"]=str(score)

# check winner..............
def checkwin(player,computer):
    if player==computer:
        updateMessage("It's a tie")
    elif player=="rock":
        if computer=="paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player=="paper":
        if computer=="scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player=="scissor":
        if computer=="rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    else:
        pass


# update choices..............
choices=["rock","paper","scissor"]
def updateChoice(x):

# for computer.............
    compChoice=choices[randint(0,2)] 
    if compChoice=="rock":
        comp_label.configure(image=cmp_rock_img)
    elif compChoice=="paper":
        comp_label.configure(image=cmp_paper_img)  
    else:
        comp_label.configure(image=cmp_scissor_img)
    

 # for user.............   

    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)  
    else:
        user_label.configure(image=scissor_img) 

    checkwin(x,compChoice)     

# buttons..............
#rock_btn=Image.open("rock_button.jpg")
rock_btn=ImageTk.PhotoImage(Image.open("rock_button.jpg"))
paper_btn=ImageTk.PhotoImage(Image.open("paper_button.jpg"))
scissor_btn=ImageTk.PhotoImage(Image.open("scissor_button.jpg"))
rock=Button(root,image=rock_btn,bg="black",command=lambda:updateChoice("rock")).grid(row=6,column=1)
paper=Button(root,image=paper_btn,bg="black",command=lambda:updateChoice("paper")).grid(row=6,column=2)
scissor=Button(root,image=scissor_btn,bg="black",command=lambda:updateChoice("scissor")).grid(row=6,column=3)

#paper=Button(root,width=20,height=2,bg="black",text="paper",fg="white").grid(row=6,column=1)
#scissor=Button(root,width=20,height=2,bg="black",text="scissor",fg="white").grid(row=6,column=2)

root.mainloop()
