from tkinter import *
from random import randrange
import turtle
from collections import Counter

turtle= turtle.Turtle() #Turtle draws letters 
win=turtle.getscreen()
turtle.shape("turtle")
turtle.down()
turtle.left(80)
turtle.forward(40)
turtle.right(80)
turtle.forward(40)
turtle.backward(40)
turtle.left(80)
turtle.backward(40)
turtle.right(80)
turtle.forward(40)
turtle.down()
turtle.left(90)
turtle.right(20)
turtle.forward(40)
turtle.right(70)
turtle.forward(4)
turtle.right(70)
turtle.forward(40)
turtle.backward(20)
turtle.right(90+20)
turtle.forward(20)
turtle.up()
turtle.backward(20)
turtle.left(110)
turtle.forward(20)
turtle.left(70)
turtle.forward(4)
turtle.down()
turtle.forward(40)
turtle.left(80)
turtle.forward(20)
turtle.left(100)
turtle.forward(40)
turtle.right(100)
turtle.forward(20)
turtle.right(80)
turtle.forward(40)
turtle.up()
turtle.forward(4)
turtle.down()
turtle.forward(40)
turtle.backward(20)
turtle.right(100)
turtle.forward(40)
turtle.right(80)
turtle.forward(20)
turtle.backward(40)
turtle.up()
turtle.backward(4)
turtle.down()
turtle.right(100)
turtle.forward(40)
turtle.right(135)
turtle.forward(50)
turtle.left(135)
turtle.forward(40)
turtle.up()
turtle.backward(40)
turtle.right(80)
turtle.forward(35)
turtle.down()
turtle.circle(22)
win.exitonclick()

horizontalchoose1 = randrange(5,9) #Generate random numbers
verticalchoose1 = randrange(1,13)
bank = 500
horizontalchoose2=randrange(6,10,2)
verticalchoose2=randrange(0, 10, 2)
horizontalchoose3 = 10
verticalchoose3=randrange(1,10,2)
horizontalchoose4 = randrange(5,10,2)
verticalchoose4= randrange(4,24,2)
horizontalchoose5= 10
verticalchoose5=randrange(0,24,2)
wonnumbers=[] #List of winning numbers

    
class numbers: #Creating the geographic representation of the chart

    def __init__(self, master):
        frame = Frame(master)
        frame.pack(fill=BOTH,side=RIGHT)

        
        self.number0 = Label(frame, text="0", bg="green",fg="black", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 3)
        self.number0.grid(row=0, column=3, columnspan =3,sticky=N+S+E+W)

        self.choice1 = Label(frame, text="1 to 18", bg="white",fg="black", font=(None,25),borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice1.grid(row=1, column=1, rowspan = 2,sticky=N+S+E+W)

        self.choice2 = Label(frame, text="1st 12", bg="white",fg="black",font=(None,25), borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice2.grid(row=1, column=2, rowspan = 4,sticky=N+S+E+W)       

        self.choice3 = Label(frame, text="EVEN", bg="white",fg="black", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice3.grid(row=3, column=1, rowspan = 2,sticky=N+S+E+W)

        self.choice4 = Label(frame, text="RED", bg="white",fg="black", font=(None,25),borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice4.grid(row=5, column=1, rowspan = 2,sticky=N+S+E+W)

        self.choice5 = Label(frame, text="BLACK", bg="white",fg="black", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice5.grid(row=7, column=1, rowspan = 2,sticky=N+S+E+W)

        self.choice6 = Label(frame, text="ODD", bg="white",fg="black", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice6.grid(row=9, column=1, rowspan = 2,sticky=N+S+E+W)

        self.choice7 = Label(frame, text="19 TO 36", bg="white",fg="black", font=(None, 20),borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice7.grid(row=11, column=1, rowspan = 2,sticky=N+S+E+W)

        self.choice8 = Label(frame, text="2nd 12", bg="white",fg="black",font=(None, 25), borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice8.grid(row=5, column=2, rowspan = 4,sticky=N+S+E+W)       

        self.choice9 = Label(frame, text="3rd 12", bg="white",fg="black",font=(None, 25), borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice9.grid(row=9, column=2,rowspan = 4, sticky=N+S+E+W)       

        self.choice10 = Label(frame, text="1st Column", bg="white",fg="black",font=(None, 15), borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice10.grid(row=13, column=3, sticky=N+S+E+W)       

        self.choice11 = Label(frame, text="2nd Column", bg="white",fg="black",font=(None, 15), borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice11.grid(row=13, column=4, sticky=N+S+E+W)       

        self.choice12 = Label(frame, text="3rd Column", bg="white",fg="black",font=(None, 15), borderwidth=1,relief=SUNKEN, height = 2, width = 6)
        self.choice12.grid(row=13, column=5, sticky=N+S+E+W)       


       

        self.number1 = Label(frame, text="1", bg="red",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number1.grid(row=1, column=3)

        self.number2 = Label(frame, text="2", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number2.grid(row=1, column=4)

        self.number3 = Label(frame, text="3", bg="red",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number3.grid(row=1, column=5)

        self.number4 = Label(frame, text="4", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number4.grid(row=2, column=3)

        self.number5 = Label(frame, text="5", bg="red",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number5.grid(row=2, column=4)

        self.number6 = Label(frame, text="6", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number6.grid(row=2, column=5)

        self.number7 = Label(frame, text="7", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number7.grid(row=3, column=3)

        self.number8 = Label(frame, text="8", bg="black",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number8.grid(row=3, column=4)
        
        self.number9 = Label(frame, text="9", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number9.grid(row=3, column=5)

        self.number10 = Label(frame, text="10", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number10.grid(row=4, column=3)

        self.number11 = Label(frame, text="11", bg="black",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number11.grid(row=4, column=4)

        self.number12 = Label(frame, text="12", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number12.grid(row=4, column=5)

        self.number13 = Label(frame, text="13", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number13.grid(row=5, column=3)

        self.number14 = Label(frame, text="14", bg="red",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number14.grid(row=5, column=4)

        self.number15 = Label(frame, text="15", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number15.grid(row=5, column=5)

        self.number16 = Label(frame, text="16", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number16.grid(row=6, column=3)

        self.number17 = Label(frame, text="17", bg="black",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number17.grid(row=6, column=4)

        self.number18 = Label(frame, text="18", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number18.grid(row=6, column=5)


        self.number19 = Label(frame, text="19", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number19.grid(row=7, column=3)

        self.number20 = Label(frame, text="20", bg="black",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number20.grid(row=7, column=4)

        self.number21 = Label(frame, text="21", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number21.grid(row=7, column=5)

        self.number22 = Label(frame, text="22", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number22.grid(row=8, column=3)

        self.number23 = Label(frame, text="23", bg="red",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number23.grid(row=8, column=4)

        self.number24 = Label(frame, text="24", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number24.grid(row=8, column=5)

        self.number25 = Label(frame, text="25", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number25.grid(row=9, column=3)

        self.number26 = Label(frame, text="26", bg="black",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number26.grid(row=9, column=4)

        self.number27 = Label(frame, text="27", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number27.grid(row=9, column=5)

        self.number28 = Label(frame, text="28", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number28.grid(row=10, column=3)

        self.number29 = Label(frame, text="29", bg="black",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number29.grid(row=10, column=4)

        self.number30 = Label(frame, text="30", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number30.grid(row=10, column=5)

        self.number31 = Label(frame, text="31", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number31.grid(row=11, column=3)

        self.number32 = Label(frame, text="32", bg="red",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number32.grid(row=11, column=4)

        self.number33 = Label(frame, text="33", bg="black",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number33.grid(row=11, column=5)

        self.number34 = Label(frame, text="34", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number34.grid(row=12, column=3)

        self.number35 = Label(frame, text="35", bg="black",fg="white", font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number35.grid(row=12, column=4)

        self.number36 = Label(frame, text="36", bg="red",fg="white",font=(None, 25),borderwidth=1,relief=SUNKEN, height = 1, width = 6)
        self.number36.grid(row=12, column=5)



root = Tk()
root.resizable(0,0)


horizontalslider = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=620,showvalue=0) #Create the slider
horizontalslider.grid(row=0,column=0)
horizontalslider.pack()

verticalslider = Scale(root, from_=0, to=26,length=580,showvalue=0)
verticalslider.grid(column=0,row = 6, rowspan = 10, columnspan=3)
verticalslider.pack(side=RIGHT)
b = numbers(root)


def single(): #Single bet
    bet = int(input("Please place your bet:"))
    global bank
    guesshorizontal = horizontalslider.get( )
    guessvertical = verticalslider.get()

    if bank > bet*2:
        choice= input("Do you want to bet another number at the same time? (y/n)")
        if choice == "y":
           if guesshorizontal == horizontalchoose1:
                if guessvertical == verticalchoose1:
                    bank += bet *35
                    print("Please choose a new value and press single2")

           else:
                bank -= bet
                print("Please choose a new value and press single2")
 
        else:
            if guesshorizontal == horizontalchoose1:
                if guessvertical == verticalchoose1:
                    bank += bet*35
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
            else:
                bank -= bet
                print("Sorry, you lost!")
                print("Now your available amount of money is " + str(bank))
            
    else:
        print("You don't have enough money.")

def single2(): #2 Single bets at the same time
    guesshorizontal1 = horizontalslider.get( )
    guessvertical1 = verticalslider.get()
    global bank
    bet = int(input("Please place your bet for the second number:"))

    if guesshorizontal1 == horizontalchoose1:
        if guessvertical1 == verticalchoose1:
            bank += bet*35
            print("Now your available amount of money is " + str(bank))
    else:
        bank -= bet
        print("Now your available amount of money is " + str(bank))

    

 
def split(): #Split bets
    bet = int(input("Please place your bet:"))
    global bank
    guesshorizontal = horizontalslider.get( )
    guessvertical = verticalslider.get()

    if bank > bet:
        if guesshorizontal == horizontalchoose2:
            if guessvertical == verticalchoose2:
                bank += bet*17
                print("Congratulations! You won!")
                print("Now your available amount of money is " + str(bank))
        else:
            bank -= bet
            print("Sorry, you lost!")
            print("Now your available amount of money is " + str(bank))
    else:
        print("You don't have enough money.")

def line(): #Line bets
    bet = int(input("Please place your bet:"))
    global bank
    guesshorizontal = horizontalslider.get( )
    guessvertical = verticalslider.get()

    if bank > bet:
        if guessvertical % 2 == 0:
            print("That's not a tenable value.")
        else:
            if guesshorizontal == horizontalchoose3:
                if guessvertical == verticalchoose3:
                    bank += bet*11
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("Now your available amount of money is " + str(bank))
 
            else:
                print('Please choose a reasonable value.')
    else:
        print("You don't have enough money.")

def corner(): #Corner bets
    bet = int(input("Please place your bet:"))
    global bank
    guesshorizontal = horizontalslider.get( )
    guessvertical = verticalslider.get()

    if bank > bet:
        if guesshorizontal == horizontalchoose4:
            if guessvertical == verticalchoose4:
                bank += bet*8
                print("Congratulations! You won!")
                print("Now your available amount of money is " + str(bank))
        else:
            bank -= bet
            print("Sorry, you lost!")
            print("Now your available amount of money is " + str(bank))
    else:
        print("You don't have enough money.Please quit.")

def street(): #Street bets
    bet = int(input("Please place your bet:"))
    global bank
    guesshorizontal = horizontalslider.get()
    guessvertical = verticalslider.get()
    if bank > bet:
        if guessvertical % 2 == 0:
            if guesshorizontal == horizontalchoose5:
                if guessvertical == verticalchoose5:
                    bank += bet*5
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("Now your available amount of money is " + str(bank))
        else:
            print("That's not a tenable value.")
    else:
        print("You don't have enough money.Please quit.")

def outsidebets(): #outside bets
    bet = int(input("Please place your bet:"))
    global bank
    guesshorizontal = horizontalslider.get()
    guessvertical = verticalslider.get()
    randomnumber = randrange(1,36)
    rednumbers = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    global wonnumbers
    wonnumbers.append(randomnumber)


    if bank > bet:
        if guesshorizontal == 3:
            if 2<= guessvertical <=8 :
                if 1<=randomnumber<=12:
                    bank += bet*2
                    print("Congratulations! You won!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))

            elif 10 <= guessvertical <= 18 :
                if 13<=randomnumber<=24:
                    bank += bet*2
                    print("Congratulations! You won!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
            elif 20 <= guessvertical <= 26 :
                if 25<=randomnumber<=36:
                    bank += bet*2
                    print("Congratulations! You won!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))

        elif guesshorizontal ==1:
            if 6 <=guessvertical<= 8:
                if randomnumber % 2 == 0:
                    bank += bet
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
            elif 18 <= guessvertical <= 20:
                if randomnumber % 2 == 0:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank += bet
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
            elif  2<=guessvertical<=4:
                if 1 <=randomnumber<= 18:
                    bank += bet
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is " + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
            elif 22 <=guessvertical<= 24:
                if 19 <= randomnumber <= 36:
                    bank += bet
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is" + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
            elif 10<= guessvertical<=12:
                if randomnumber in rednumbers:
                    bank += bet
                    print("Congratulations! You won!")
                    print("The chosen number is" + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is" + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
            elif 14<= guessvertical <= 16:
                if randomnumber in rednumbers:
                    bank -= bet
                    print("Sorry, you lost!")
                    print("The chosen number is" + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank += bet
                    print("Congratulations! You won!")
                    print("The chosen number is" + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
                     
        elif guessvertical == 26:
            if guesshorizontal == 5:
                if (randomnumber-1) % 3 == 0:
                    bank += bet*2
                    print("The number is" + str(randomnumber))
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
                else:
                    print("The number is" + str(randomnumber))
                    print("Sorry, you lost!")
                    print("The chosen number is" + str(randomnumber))
                    print("Now your available amount of money is " + str(bank))
            elif guesshorizontal == 7:
                if (randomnumber-2) % 3 == 0:
                    bank += bet*2
                    print("The number is" + str(randomnumber))
                    print("Congradulations! You won!")
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("The number is" + str(randomnumber))
                    print("Sorry, you lost!")
                    print("Now your available amount of money is " + str(bank))
            elif guesshorizontal == 9:
                if randomnumber % 3 == 0:
                    bank += bet*2
                    print("The number is" + str(randomnumber))
                    print("Congratulations! You won!")
                    print("Now your available amount of money is " + str(bank))
                else:
                    bank -= bet
                    print("The number is" + str(randomnumber))
                    print("Sorry, you lost!")
                    print("Now your available amount of money is " + str(bank))                    
                     
    else:
        print("You don't have enough money.Please quit.")
    return
        
menu = Menu(root)
root.config(menu=menu)

def won(): #Tracking winning numbers
    global wonnumbers
    print("Winning numbers are " + str(wonnumbers))
    b = Counter(wonnumbers)
    print ("The most common one is " + str(b.most_common(1)))
    print ("Every number's appearance frequency is " + str(b))
    
subMenu = Menu(menu) #Create the drop down menu
menu.add_cascade(label="Bet Type",menu=subMenu)
subMenu.add_command(label="Single Bets",command=single)
subMenu.add_command(label="Split Bets",command=split)
subMenu.add_command(label="Corner Bets",command=corner)
subMenu.add_command(label="Line Bets",command=line)
subMenu.add_command(label="Street Bets",command=street)
subMenu.add_command(label="Outside Bets",command=outsidebets)
subMenu.add_command(label="Print Winning Numbers",command=won)
subMenu.add_command(label="Single 2 Bets",command=single2)



root.mainloop()


    
