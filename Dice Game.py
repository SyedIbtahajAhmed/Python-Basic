import random
#============================
#============================
def dice1():
	print(" ___________")
	print("|           |")
	print("|           |")
	print("|     0     |")
	print("|           |")
	print("|___________|")

#============================
#============================
def dice2():
	print(" ___________")
	print("|           |")
	print("|  0        |")
	print("|           |")
	print("|        0  |")
	print("|___________|")
	
#============================
#============================
def dice3():
	print(" ___________")
	print("|           |")
	print("|  0        |")
	print("|     0     |")
	print("|        0  |")
	print("|___________|")

#============================
#============================
def dice4():
	print(" ___________")
	print("|           |")
	print("|  0     0  |")
	print("|           |")
	print("|  0     0  |")
	print("|___________|")

#============================
#============================
def dice5():
	print(" ___________")
	print("|           |")
	print("|  0     0  |")
	print("|     0     |")
	print("|  0     0  |")
	print("|___________|")

#============================
#============================
def dice6():
	print(" ___________")
	print("|           |")
	print("|  0     0  |")
	print("|  0     0  |")
	print("|  0     0  |")
	print("|___________|")

#============================
#============================	

result=0
start = str(input("\nPress Any Key To Continue The Program Or Press Q To Quit The Program :"))

if(start!="q"):
    print("\n\nHERE ARE SOME RULES TO PLAY THE GAME :","\n============================================================================================================","\n============================================================================================================")
    print("\n\n1.) The name of the game is Petals Around the Rose.","\n2.) The name of the game is important.","\n3.) The computer will roll five dice and ask you to guess the score for the roll.","\n4.) The score will always be zero or an even number.","\n5.) Your mission is to work out how the computer calculates the score and become a Potentate of the Rose.")
    rolling = str(input("\n\nPress Any Key To Roll The Dices And Play The Game Or Press Q To Quit The Program :"))
    
while(rolling!="q"):
    result=0
    for i in range(0,6):
        roll=random.randint(1,6)
            
        if roll==1:
            dice1()
        elif roll==2:
            dice2()
        elif roll==3:
        
            dice3()
            result=result+2
        elif roll==4:
            dice4()
        elif roll==5:
            dice5()
            result=result+4
        else:
            dice6()
    print("\n============================================================================================================","\n============================================================================================================")
    guess = int(input("\n\nEnter Your Guess :"))
    if(guess==result):
        print("\n* You Are Right")
        print ("\n* The Result Is: "+str(result))
        print("\n\n============================================================================================================","\n============================================================================================================")
        rolling = str(input("\n\nPress Any Key To Again Roll The Dices And Play The Game Or Press Q To Quit The Program :"))
    else:
        print("\n* Your Are Wrong")
        print ("\n* The Result Is: "+str(result))
        print("\n\n============================================================================================================","\n============================================================================================================")
        rolling = str(input("\n\nPress Any Key To Again Roll The Dices And Play The Game Or Press Q To Quit The Program :"))
#========================================================================================================
#========================================================================================================
