import sys
from collections import namedtuple 

points=0

def struct_player():
    global name
    name=input("Please enter your name ")
    
    
def question1():
    global points
    print("Thank you for accepting to play the game!")
    answer1= input("Question 1: Which river is the largest in terms of volume in the world?")

    if answer1.lower() == "amazon":
        points+=5
        print("\033[32m Correct!\033[m") 


    else: 
        print("\033[31mWrong Answer\033[m")
        print("The correct answer would be the Amazon")
        

def question2():
    global points
    answer2= input("Question 2: What color do you get by mixing the colours Red and Yellow?")
    if answer2.lower() == "orange":
        points += 5
        print("\033[32m Correct!\033[m")
    
    else : 
        print("\033[31mWrong Answer\033[m")
        print("The correct answer would be Orange")
        if points<2: points=0
        else: points-=2
        
    
        
def question3():
    global points
    answer3= input("Question 3: Who is credited for inventing the radio?")
    if answer3.lower() == "marconni":
        points += 5
        print("\033[32m Correct!\033[m")
    
    else : 
        print("\033[31mWrong Answer\033[m")
        print("The correct answer would be Marconni")
        if points<2: points=0
        else: points-=2
    

def question4():
    global points
    answer4= input("Question 4: Who wrote the famous novel '1984'?")
    if answer4.lower().replace(" ","") == "georgeorwell":
        points += 5
        
        print("\033[32m Correct!\033[m")
    
    else : 
        print("\033[31mWrong Answer\033[m")
        print("The correct answer would be George Orwell")
        if points<2: points=0
        else: points-=2
          

def question5():
    global points
    answer5= input("Question 5: Which is the smallest country in the world by land area?")
    if answer5.lower() == "vatican":
        points += 5
        print("\033[32m Correct!\033[m")
    
    else : 
        print("\033[31mWrong Answer\033[m")
        print("The correct answer would be Vatican")
        if points<2: points=0
        else: points-=2 

def endgame():
    global name, points
    print("Congratulations "+ name +", you have finished the game")
    print("Your overall score is: ", points)
    print("Thank you so much for playing!")

def welcome():
    print("Welcome to my game! This is my first code ever in Python")
    print("The rules are simple:")
    input()
    print("1. I will ask a series of questions and you're asked to write on the terminal")
    input()
    print("2. For each correct answer, 5 points will be added to your overall score")   
    input()
    print("3. For each wrong answer, 2 points will be deducted ")
    input()
    print("4. Don't worry, the score won't go negative if you have less than 2 points")
    input()
    return

play= input("Do you wish to play the Quiz? ")

if play.lower() == "yes" or play.lower() == "y":

    points=0
    struct_player()
    welcome()
    question1()
    question2()
    question3()
    question4()
    question5()
    endgame()
    sys.exit()    
 
else : print("Ok! See you, then!")  
sys.exit()

