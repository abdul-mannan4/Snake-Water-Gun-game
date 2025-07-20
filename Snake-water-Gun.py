import random
import os
import time
choice1={'s':1,'w':2,'g':3}
def mainpage():
    print("=========================================================")
    print(">>>>>>>>>>>>>Welcome to Snake Water Gun Game<<<<<<<<<<<<<")
    print("=========================================================")
    print("              1. For Snake")
    print("              2. For Water")
    print("              3. For Gun")
    print("              4. EXIT")
    print("==========================================================")
    print("")

mainpage()
attemptsno=int(input("Enter the number of attempts you want to play: "))
os.system('cls')
yourscore=0
computerscore=0
for i in range(0,attemptsno):
    mainpage()
    print(f"Round: {i+1}")
    yourchoice=eval(input("Enter your Choice: "))
    computer_choice=random.choice(list(choice1.values()))
    print(f"Computer choice: {computer_choice}")
    if(yourchoice==1 and computer_choice==2):
        yourscore+=1
        print(f"Your Point!                      Your Score: {yourscore}")
    elif(yourchoice==2 and computer_choice==1):
        computerscore+=1
        print(f"Computer Point!                  Computer score: {computerscore}")
    elif(yourchoice==1 and computer_choice==3):
        computerscore+=1
        print(f"Computer Point!                  Computer score: {computerscore}")
    elif(yourchoice==3 and computer_choice==1):
        yourscore+=1
        print(f"Your Point!                      Your Score: {yourscore}")
    elif(yourchoice==2 and computer_choice==3):
        yourscore+=1
        print(f"Your Point!                      Your Score: {yourscore}")
    elif(yourchoice==3 and computer_choice==2):
        computerscore+=1
        print(f"Computer Point!                  Computer score: {computerscore}")
    elif(yourchoice==computer_choice):
        print("No point, Same choice")
    elif(yourchoice==4):
        break
    time.sleep(6)
    os.system('cls')

if(yourscore>computerscore):
    print("Congratulations, You won!")
    print(f"Your Score is: {yourscore}")
    print(f"Computer Score is: {computerscore}")
if(yourscore<computerscore):
    print("Bad, You Lost!")
    print(f"Computer Score is: {computerscore}")
    print(f"Your Score is: {yourscore}")

if(yourscore==computerscore):
    print("Match Tie")
    print(f"Your Score is: {yourscore}")
    print(f"Computer Score is: {computerscore}")

