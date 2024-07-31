from tkinter import*
from PIL import Image,ImageTk

root=Tk()
root.title("Quiz")
root['bg']='teal'


label=Label(root,text='<<<...Welcome to the QUIZ...>>>',font=('Arial',35),bg='teal')
label.place(x=420,y=100)
label1=Label(root,text='Enter Name :',font=('Arial',20,"bold"),bg='teal')
label1.place(x=450,y=300)
entry1=Entry(root,font=('Arial',20))
entry1.place(x=650,y=300)
entry1.focus()
rules=Label(root,text='Rules :-',font=('Arial',25,"bold","underline"),bg='teal')
rules.place(x=50,y=500)
r1=Label(root,text='# There is no previous button, you can not back to the last question, so read and select an answer carefully.',font=('Arial',15,"bold"),bg='teal')
r1.place(x=50,y=600)
r2=Label(root,text='# Each question carries equal marks that is: 1',font=('Arial',15,"bold"),bg='teal')
r2.place(x=50,y=650)
r3=Label(root,text='# There is no negative marking, if you select wrong answer, 0 mark will be added to your score.',font=('Arial',15,"bold"),bg='teal')
r3.place(x=50,y=700)
r4=Label(root,text='# At final page you will see total winning points and all questions with their correct answer ',font=('Arial',15,"bold"),bg='teal')
r4.place(x=50,y=750)
r5=Label(root,text='# No time limit',font=('Arial',15,"bold"),bg='teal')
r5.place(x=50,y=800)

img1=ImageTk.PhotoImage(Image.open("border.png"))
img2=ImageTk.PhotoImage(Image.open("city.jpg"))
img3=ImageTk.PhotoImage(Image.open("continent.jpg"))
img4=ImageTk.PhotoImage(Image.open("fruits.jpg"))
img5=ImageTk.PhotoImage(Image.open("map1.jpg"))
img6=ImageTk.PhotoImage(Image.open("tower.jpg"))
img7=ImageTk.PhotoImage(Image.open("water.jpg"))
img8=ImageTk.PhotoImage(Image.open("book.jpg"))
img9=ImageTk.PhotoImage(Image.open("money.png"))
img10=ImageTk.PhotoImage(Image.open("lion.jpg"))
img11=ImageTk.PhotoImage(Image.open("expire.jpg"))
img12=ImageTk.PhotoImage(Image.open("seeds.jpg"))
img13=ImageTk.PhotoImage(Image.open("sleep.jpg"))
img14=ImageTk.PhotoImage(Image.open("monalisa.jpg"))
img15=ImageTk.PhotoImage(Image.open("google.jpg"))

count=0

def que1():

    name=entry1.get()
    global count
    count+=1
    label2=Label(root,text='Question 1',font=('Arial',20),bg='teal')
    label2.place(x=60,y=40)
    label3=Label(root,text='Q :: The first person to draw the map of earth ?',font=('Arial',20),bg='teal')
    label3.place(x=300,y=250)
    label4=Label(root,image=img5)
    label4.place(x=840,y=360)
    
    
    def que2():
        global count
        count+=1
        labelz=Label(root)
        labelz.pack()
        labelz.after(10,fun2)

    def fun2():
        label5=Label(root,text='Question 2',font=('Arial',20),bg='teal')
        label5.place(x=60,y=40)
        label6=Label(root,text='Q :: The first country to print book ?',font=('Arial',20),bg='teal')
        label6.place(x=300,y=250)
        label7=Label(root,image=img8)
        label7.place(x=840,y=360)

        def que3():
            global count
            count+=1  
            labelz1=Label(root)
            labelz1.pack()
            labelz1.after(10,fun3)  

        def fun3():
            label8=Label(root,text='Question 3',font=('Arial',20),bg='teal')
            label8.place(x=60,y=40)
            label9=Label(root,text='Q :: The first country to issue paper currency ?',font=('Arial',20),bg='teal')
            label9.place(x=300,y=250)
            label10=Label(root,image=img9)
            label10.place(x=840,y=360)

            def que4():
                global count
                count+=1  
                labelz2=Label(root)
                labelz2.pack()
                labelz2.after(10,fun4) 

            def fun4():
                label11=Label(root,text='Question 4',font=('Arial',20),bg='teal')
                label11.place(x=60,y=40)
                label12=Label(root,text='Q :: Which is the largest continent on Earth ?',font=('Arial',20),bg='teal')
                label12.place(x=300,y=250)
                label13=Label(root,image=img3)
                label13.place(x=840,y=360)

                def que5():
                    global count
                    count+=1
                    labelz3=Label(root)
                    labelz3.pack()
                    labelz3.after(10,fun5)    

                def fun5():
                    label14=Label(root,text='Question 5',font=('Arial',20),bg='teal')
                    label14.place(x=60,y=40)
                    label15=Label(root,text='Q :: Which lion hunts more, male or female ?',font=('Arial',20),bg='teal')
                    label15.place(x=300,y=250)
                    label16=Label(root,image=img10)
                    label16.place(x=840,y=360)

                    def que6():
                        global count
                        count+=1
                        labelz4=Label(root)
                        labelz4.pack()
                        labelz4.after(10,fun6) 

                    def fun6():
                        label17=Label(root,text='Question 6',font=('Arial',20),bg='teal')
                        label17.place(x=60,y=40)
                        label18=Label(root,text='Q :: A city located on two continents ?',font=('Arial',20),bg='teal')
                        label18.place(x=300,y=250)
                        label19=Label(root,image=img2)
                        label19.place(x=840,y=360)

                        def que7():
                            global count
                            count+=1
                            labelz5=Label(root)
                            labelz5.pack()
                            labelz5.after(10,fun7) 

                        def fun7():
                            label20=Label(root,text='Question 7',font=('Arial',20),bg='teal')
                            label20.place(x=60,y=40)
                            label21=Label(root,text='Q :: Which countries share the largest border ?',font=('Arial',20),bg='teal')
                            label21.place(x=300,y=250)
                            label22=Label(root,image=img1)
                            label22.place(x=840,y=360)

                            def que8():
                                global count
                                count+=1
                                labelz6=Label(root)
                                labelz6.pack()
                                labelz6.after(10,fun8)

                            def fun8():
                                label23=Label(root,text='Question 8',font=('Arial',20),bg='teal')
                                label23.place(x=60,y=40)
                                label24=Label(root,text='Q :: Name the tallest building in the world ?',font=('Arial',20),bg='teal')
                                label24.place(x=300,y=250)
                                label25=Label(root,image=img6)
                                label25.place(x=840,y=360)

                                def que9():
                                    global count
                                    count+=1
                                    labelz7=Label(root)
                                    labelz7.pack()
                                    labelz7.after(10,fun9)

                                def fun9():
                                    label26=Label(root,text='Question 9',font=('Arial',20),bg='teal')
                                    label26.place(x=60,y=40)
                                    label27=Label(root,text="Q :: Which fruit's seed is on the outside ?",font=('Arial',20),bg='teal')
                                    label27.place(x=300,y=250)
                                    label28=Label(root,image=img12)
                                    label28.place(x=840,y=360)

                                    def que10():
                                        global count
                                        count+=1
                                        labelz8=Label(root)
                                        labelz8.pack()
                                        labelz8.after(10,fun10)

                                    def fun10():
                                        label29=Label(root,text='Question 10',font=('Arial',20),bg='teal')
                                        label29.place(x=60,y=40)
                                        label30=Label(root,text="Q :: Which fruit has the highest water content ?",font=('Arial',20),bg='teal')
                                        label30.place(x=300,y=250)
                                        label31=Label(root,image=img7)
                                        label31.place(x=840,y=360)

                                        def que11():
                                            global count
                                            count+=1
                                            labelz9=Label(root)
                                            labelz9.pack()
                                            labelz9.after(10,fun11)

                                        def fun11():
                                            label32=Label(root,text='Question 11',font=('Arial',20),bg='teal')
                                            label32.place(x=60,y=40)
                                            label33=Label(root,text="Q :: What food will never spoil or expire ?",font=('Arial',20),bg='teal')
                                            label33.place(x=300,y=250)
                                            label34=Label(root,image=img11)
                                            label34.place(x=840,y=360)

                                            def que12():
                                                global count
                                                count+=1
                                                labelz10=Label(root)
                                                labelz10.pack()
                                                labelz10.after(10,fun12)

                                            def fun12():
                                                label35=Label(root,text='Question 12',font=('Arial',20),bg='teal')
                                                label35.place(x=60,y=40)
                                                label36=Label(root,text="Q :: What is the most popular fruit in the world ?",font=('Arial',20),bg='teal')
                                                label36.place(x=300,y=250)
                                                label37=Label(root,image=img4)
                                                label37.place(x=840,y=360)

                                                def que13():
                                                    global count
                                                    count+=1
                                                    labelz11=Label(root)
                                                    labelz11.pack()
                                                    labelz11.after(10,fun13)

                                                def fun13():
                                                    label38=Label(root,text='Question 13',font=('Arial',20),bg='teal')
                                                    label38.place(x=60,y=40)
                                                    label39=Label(root,text="Q :: Most people fall asleep in ____ minutes.",font=('Arial',20),bg='teal')
                                                    label39.place(x=300,y=250)
                                                    label40=Label(root,image=img13)
                                                    label40.place(x=840,y=360)

                                                    def que14():
                                                        global count
                                                        count+=1
                                                        labelz12=Label(root)
                                                        labelz12.pack()
                                                        labelz12.after(10,fun14)

                                                    def fun14():
                                                        label41=Label(root,text='Question 14',font=('Arial',20),bg='teal')
                                                        label41.place(x=60,y=40)
                                                        label42=Label(root,text="Q :: Who painted the Mona Lisa ?",font=('Arial',20),bg='teal')
                                                        label42.place(x=300,y=250)
                                                        label43=Label(root,image=img14)
                                                        label43.place(x=840,y=360)

                                                        def que15():
                                                            global count
                                                            count+=1
                                                            labelz13=Label(root)
                                                            labelz13.pack()
                                                            labelz13.after(10,fun15)

                                                        def fun15():
                                                            label44=Label(root,text='Question 15',font=('Arial',20),bg='teal')
                                                            label44.place(x=60,y=40)
                                                            label45=Label(root,text='Q :: What color is the "G" in the google ?',font=('Arial',20),bg='teal')
                                                            label45.place(x=300,y=250)
                                                            label46=Label(root,image=img15)
                                                            label46.place(x=840,y=360)

                                                            def final():
                                                                global count
                                                                count+=1
                                                                #percentage=(count/15)*100
                                                                labelz14=Label(root)
                                                                labelz14.pack()
                                                                labelz14.after(10,funfinal)

                                                            def funfinal():
                                                                percentage=(count/15)*100
                                                                label47=Label(root,text='Total score :',font=('Arial',20),bg='teal')
                                                                label47.place(x=580,y=50)
                                                                label50=Label(root,text=count,font=('Arial',20),bg='teal')
                                                                label50.place(x=800,y=50)
                                                                label81=Label(root,text='Percentage :',font=('Arial',20),bg='teal')
                                                                label81.place(x=580,y=100)
                                                                label82=Label(root,text=percentage,font=('Arial',20),bg='teal')
                                                                label82.place(x=800,y=100)
                                                                label48=Label(root,text='Name :',font=('Arial',20),bg='teal')
                                                                label48.place(x=580,y=0)
                                                                label49=Label(root,text=name.upper(),font=('Arial',20),bg='teal')
                                                                label49.place(x=800,y=0)
                                                                label51=Label(root,text='1..The first person to draw the map of earth ?',font=('Arial',20),fg='navy',bg='teal')
                                                                label51.place(x=10,y=150)
                                                                label52=Label(root,text='2..The first country to print book ?',font=('Arial',20),fg='white',bg='teal')
                                                                label52.place(x=10,y=200)
                                                                label53=Label(root,text='3..The first country to issue paper currency ?',font=('Arial',20),fg='navy',bg='teal')
                                                                label53.place(x=10,y=250)
                                                                label54=Label(root,text='4..Which is the largest continent on Earth ?',font=('Arial',20),fg='white',bg='teal')
                                                                label54.place(x=10,y=300)
                                                                label55=Label(root,text='5..Which lion hunts more, male or female ?',font=('Arial',20),fg='navy',bg='teal')
                                                                label55.place(x=10,y=350)
                                                                label56=Label(root,text='6..A city located on two continents ?',font=('Arial',20),fg='white',bg='teal')
                                                                label56.place(x=10,y=400)
                                                                label57=Label(root,text='7.. Which countries share the largest border ?',font=('Arial',20),fg='navy',bg='teal')
                                                                label57.place(x=10,y=450)
                                                                label58=Label(root,text='8..Name the tallest building in the world ?',font=('Arial',20),fg='white',bg='teal')
                                                                label58.place(x=10,y=500)
                                                                label59=Label(root,text="9.. Which fruit's seed is on the outside ?",font=('Arial',20),fg='navy',bg='teal')
                                                                label59.place(x=10,y=550)
                                                                label60=Label(root,text="10..Which fruit has the highest water content ?",font=('Arial',20),fg='white',bg='teal')
                                                                label60.place(x=10,y=600)
                                                                label61=Label(root,text='11..What food will never spoil or expire ?',font=('Arial',20),fg='navy',bg='teal')
                                                                label61.place(x=10,y=650)
                                                                label62=Label(root,text='12..What is the most popular fruit in the world ?',font=('Arial',20),fg='white',bg='teal')
                                                                label62.place(x=10,y=700)
                                                                label63=Label(root,text='13..Most people fall asleep in ____ minutes.',font=('Arial',20),fg='navy',bg='teal')
                                                                label63.place(x=10,y=750)
                                                                label64=Label(root,text='14..Who painted the Mona Lisa ?',font=('Arial',20),fg='white',bg='teal')
                                                                label64.place(x=10,y=800)
                                                                label65=Label(root,text='15..What color is the "G" in the google ?',font=('Arial',20),fg='navy',bg='teal')
                                                                label65.place(x=10,y=850)
                                                                label66=Label(root,text='Anaximander',font=('Arial',20),fg='navy',bg='teal')
                                                                label66.place(x=1000,y=150)
                                                                label67=Label(root,text='China',font=('Arial',20),fg='white',bg='teal')
                                                                label67.place(x=1000,y=200)
                                                                label68=Label(root,text='China',font=('Arial',20),fg='navy',bg='teal')
                                                                label68.place(x=1000,y=250)
                                                                label69=Label(root,text='Asia',font=('Arial',20),fg='white',bg='teal')
                                                                label69.place(x=1000,y=300)
                                                                label70=Label(root,text='Female',font=('Arial',20),fg='navy',bg='teal')
                                                                label70.place(x=1000,y=350)
                                                                label71=Label(root,text='Istanbul',font=('Arial',20),fg='white',bg='teal')
                                                                label71.place(x=1000,y=400)
                                                                label72=Label(root,text='US-Canada',font=('Arial',20),fg='navy',bg='teal')
                                                                label72.place(x=1000,y=450)
                                                                label73=Label(root,text='Burj Khalifa',font=('Arial',20),fg='white',bg='teal')
                                                                label73.place(x=1000,y=500)
                                                                label74=Label(root,text='Strawberry',font=('Arial',20),fg='navy',bg='teal')
                                                                label74.place(x=1000,y=550)
                                                                label75=Label(root,text='cucumber',font=('Arial',20),fg='white',bg='teal')
                                                                label75.place(x=1000,y=600)
                                                                label76=Label(root,text='Honey',font=('Arial',20),fg='navy',bg='teal')
                                                                label76.place(x=1000,y=650)
                                                                label77=Label(root,text='Banana',font=('Arial',20),fg='white',bg='teal')
                                                                label77.place(x=1000,y=700)
                                                                label78=Label(root,text='7',font=('Arial',20),fg='navy',bg='teal')
                                                                label78.place(x=1000,y=750)
                                                                label79=Label(root,text='Leonardo da vinci',font=('Arial',20),fg='white',bg='teal')
                                                                label79.place(x=1000,y=800)
                                                                label80=Label(root,text='Blue',font=('Arial',20),fg='navy',bg='teal')
                                                                label80.place(x=1000,y=850)
                                                                
                                                                label44.destroy()
                                                                label45.destroy()
                                                                label46.destroy()
                                                                button72.destroy()
                                                                button73.destroy()
                                                                button74.destroy()
                                                                button75.destroy()
                                                               
                                                            button72=Button(root,text='Red',font=('Arial',20),bg='teal',command=funfinal)
                                                            button72.place(x=340,y=360)
                                                            button73=Button(root,text='Yellow',font=('Arial',20),bg='teal',command=funfinal)
                                                            button73.place(x=340,y=440)
                                                            button74=Button(root,text='Blue',font=('Arial',20),bg='teal',command=final)
                                                            button74.place(x=340,y=520)
                                                            button75=Button(root,text='Green',font=('Arial',20),bg='teal',command=funfinal)
                                                            button75.place(x=340,y=600)

                                                            label41.destroy()
                                                            label42.destroy()
                                                            label43.destroy()
                                                            button67.destroy()
                                                            button68.destroy()
                                                            button69.destroy()
                                                            button70.destroy()
                                                            
                                                        button67=Button(root,text='Leonardo da vinci',font=('Arial',20),bg='teal',command=que15)
                                                        button67.place(x=340,y=360)
                                                        button68=Button(root,text='Pablo Picasso',font=('Arial',20),bg='teal',command=fun15)
                                                        button68.place(x=340,y=440)
                                                        button69=Button(root,text='Claude monet',font=('Arial',20),bg='teal',command=fun15)
                                                        button69.place(x=340,y=520)
                                                        button70=Button(root,text='Michelangelo',font=('Arial',20),bg='teal',command=fun15)
                                                        button70.place(x=340,y=600)

                                                        label38.destroy()
                                                        label39.destroy()
                                                        label40.destroy()
                                                        button63.destroy()
                                                        button64.destroy()
                                                        button65.destroy()
                                                        button66.destroy()
                                                        
                                                    button66=Button(root,text='5',font=('Arial',20),bg='teal',command=fun14)
                                                    button66.place(x=340,y=360)
                                                    button63=Button(root,text='7',font=('Arial',20),bg='teal',command=que14)
                                                    button63.place(x=340,y=440)
                                                    button64=Button(root,text='8',font=('Arial',20),bg='teal',command=fun14)
                                                    button64.place(x=340,y=520)
                                                    button65=Button(root,text='10',font=('Arial',20),bg='teal',command=fun14)
                                                    button65.place(x=340,y=600)

                                                    label35.destroy()
                                                    label36.destroy()
                                                    label37.destroy()
                                                    button.destroy()
                                                    button57.destroy()
                                                    button58.destroy()
                                                    button59.destroy()
                                                    button60.destroy()
                                                    button61.destroy()
                                                    
                                                button=Button(root,text='Mango',font=('Arial',15),bg='teal',command=fun13)
                                                button.place(x=340,y=330)
                                                button57=Button(root,text='Strawberry',font=('Arial',15),bg='teal',command=fun13)
                                                button57.place(x=340,y=390)
                                                button58=Button(root,text='Banana',font=('Arial',15),bg='teal',command=que13)
                                                button58.place(x=340,y=450)
                                                button59=Button(root,text='Grapes',font=('Arial',15),bg='teal',command=fun13)
                                                button59.place(x=340,y=510)
                                                button60=Button(root,text='Apple',font=('Arial',15),bg='teal',command=fun13)
                                                button60.place(x=340,y=570)
                                                button61=Button(root,text='Orange',font=('Arial',15),bg='teal',command=fun13)
                                                button61.place(x=340,y=630)

                                                label32.destroy()
                                                label33.destroy()
                                                label34.destroy()
                                                button51.destroy()
                                                button52.destroy()
                                                button53.destroy()
                                                button54.destroy()
                                                
                                            button51=Button(root,text='Honey',font=('Arial',20),bg='teal',command=que12)
                                            button51.place(x=340,y=360)
                                            button52=Button(root,text='Salt',font=('Arial',20),bg='teal',command=fun12)
                                            button52.place(x=340,y=440)
                                            button53=Button(root,text='Vinegar',font=('Arial',20),bg='teal',command=fun12)
                                            button53.place(x=340,y=520)
                                            button54=Button(root,text='Rice',font=('Arial',20),bg='teal',command=fun12)
                                            button54.place(x=340,y=600)

                                            label29.destroy()
                                            label30.destroy()
                                            label31.destroy()
                                            button46.destroy()
                                            button47.destroy()
                                            button48.destroy()
                                            button49.destroy()
                                            
                                        button46=Button(root,text='Cucumber',font=('Arial',20),bg='teal',command=que11)
                                        button46.place(x=340,y=360)
                                        button47=Button(root,text='Water melon',font=('Arial',20),bg='teal',command=fun11)
                                        button47.place(x=340,y=440)
                                        button48=Button(root,text='Orange',font=('Arial',20),bg='teal',command=fun11)
                                        button48.place(x=340,y=520)
                                        button49=Button(root,text='Pineapple',font=('Arial',20),bg='teal',command=fun11)
                                        button49.place(x=340,y=600)

                                        label26.destroy()
                                        label27.destroy()
                                        label28.destroy()
                                        button42.destroy()
                                        button43.destroy()
                                        button44.destroy()
                                        button45.destroy()
                                        
                                    button42=Button(root,text='Raspberry',font=('Arial',20),bg='teal',command=fun10)
                                    button42.place(x=340,y=360)
                                    button43=Button(root,text='Blueberry',font=('Arial',20),bg='teal',command=fun10)
                                    button43.place(x=340,y=440)
                                    button44=Button(root,text='Strawberry',font=('Arial',20),bg='teal',command=que10)
                                    button44.place(x=340,y=520)
                                    button45=Button(root,text='Blackberry',font=('Arial',20),bg='teal',command=fun10)
                                    button45.place(x=340,y=600)

                                    label23.destroy()
                                    label24.destroy()
                                    label25.destroy()
                                    button27.destroy()
                                    button28.destroy()
                                    button29.destroy()
                                    button30.destroy()
                                    
                                button27=Button(root,text='Burj khalifa',font=('Arial',20),bg='teal',command=que9)
                                button27.place(x=340,y=360)
                                button28=Button(root,text='Eiffel Tower',font=('Arial',20),bg='teal',command=fun9)
                                button28.place(x=340,y=440)
                                button29=Button(root,text='Shanghai Tower',font=('Arial',20),bg='teal',command=fun9)
                                button29.place(x=340,y=520)
                                button30=Button(root,text='Empire state building',font=('Arial',20),bg='teal',command=fun9)
                                button30.place(x=340,y=600)

                                label20.destroy()
                                label21.destroy()
                                label22.destroy()
                                button37.destroy()
                                button38.destroy()
                                button39.destroy()
                                button40.destroy()
                                
                            button37=Button(root,text='Mongolia-Russia',font=('Arial',20),bg='teal',command=fun8)
                            button37.place(x=340,y=360)
                            button38=Button(root,text='US-Canada',font=('Arial',20),bg='teal',command=que8)
                            button38.place(x=340,y=440)
                            button39=Button(root,text='China-Mongolia',font=('Arial',20),bg='teal',command=fun8)
                            button39.place(x=340,y=520)
                            button40=Button(root,text='Kazakhstan-Russia',font=('Arial',20),bg='teal',command=fun8)
                            button40.place(x=340,y=600)

                            label17.destroy()
                            label18.destroy()
                            label19.destroy()
                            button31.destroy()
                            button32.destroy()
                            button33.destroy()
                            
                        button31=Button(root,text='Istanbul',font=('Arial',20),bg='teal',command=fun7)
                        button31.place(x=340,y=360)
                        button32=Button(root,text='Cairo',font=('Arial',20),bg='teal',command=fun7)
                        button32.place(x=340,y=440)
                        button33=Button(root,text='Moscow',font=('Arial',20),bg='teal',command=fun7)
                        button33.place(x=340,y=520)

                        label14.destroy()
                        label15.destroy()
                        label16.destroy()
                        button25.destroy()
                        button26.destroy()
                                          
                    button25=Button(root,text='Male',font=('Arial',20),bg='teal',command=fun6)
                    button25.place(x=340,y=380)
                    button26=Button(root,text='Female',font=('Arial',20),bg='teal',command=que6)
                    button26.place(x=340,y=500)

                    label11.destroy()
                    label12.destroy()
                    label13.destroy()
                    button19.destroy()
                    button20.destroy()
                    button21.destroy()
                    button22.destroy()
                                   
                button19=Button(root,text='Europe',font=('Arial',20),bg='teal',command=fun5)
                button19.place(x=340,y=360)
                button20=Button(root,text='South America',font=('Arial',20),bg='teal',command=fun5)
                button20.place(x=340,y=440)
                button21=Button(root,text='Asia',font=('Arial',20),bg='teal',command=que5)
                button21.place(x=340,y=520)
                button22=Button(root,text='Africa',font=('Arial',20),bg='teal',command=fun5)
                button22.place(x=340,y=600)

                label8.destroy()
                label9.destroy()
                label10.destroy()
                button13.destroy()
                button14.destroy()
                button15.destroy()
                button16.destroy()
                           
            button13=Button(root,text='Britain',font=('Arial',20),bg='teal',command=fun4)
            button13.place(x=340,y=360)
            button14=Button(root,text='China',font=('Arial',20),bg='teal',command=que4)
            button14.place(x=340,y=440)
            button15=Button(root,text='France',font=('Arial',20),bg='teal',command=fun4)
            button15.place(x=340,y=520)
            button16=Button(root,text='UK',font=('Arial',20),bg='teal',command=fun4)
            button16.place(x=340,y=600)
 
            label5.destroy()
            label6.destroy()
            label7.destroy()
            button7.destroy()
            button8.destroy()
            button9.destroy()
            button10.destroy()
                   
        button7=Button(root,text='India',font=('Arial',20),bg='teal',command=fun3)
        button7.place(x=340,y=360)
        button8=Button(root,text='China',font=('Arial',20),bg='teal',command=que3)
        button8.place(x=340,y=440)
        button9=Button(root,text='Japan',font=('Arial',20),bg='teal',command=fun3)
        button9.place(x=340,y=520)
        button10=Button(root,text='USA',font=('Arial',20),bg='teal',command=fun3)
        button10.place(x=340,y=600)

        label2.destroy()
        label3.destroy()
        label4.destroy()
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
           
    button1=Button(root,text='Anaximander',font=('Arial',20),bg='teal',command=que2)
    button1.place(x=340,y=360)
    button2=Button(root,text='Phythagoras',font=('Arial',20),bg='teal',command=fun2)
    button2.place(x=340,y=440)
    button3=Button(root,text='Thales',font=('Arial',20),bg='teal',command=fun2)
    button3.place(x=340,y=520)
    button4=Button(root,text='Heraclitus',font=('Arial',20),bg='teal',command=fun2)
    button4.place(x=340,y=600)
    
    label1.destroy()
    label.destroy()
    entry1.destroy()
    button.destroy()
    rules.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()

button=Button(root,text='SUBMIT',font=('Arial',20,"bold"),bg='teal',command=que1)
button.place(x=650,y=400)

root.mainloop()



            