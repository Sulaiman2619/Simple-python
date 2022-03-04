from ast import Global, While
from glob import glob
import random as rd
import sys



min = ""
max = ""
NumberToGuess = ""
UserGuess = -1
Guess = ""

# class bcolors:
#     RED = '\033[31m'
#     Blue = '\033[34m'
#     Green = '\033[32m'
#     ENDC = '\033[0m'

    
def Numbermin ():
    global min
    try :
        min = int(input("Enter number min : "))
    except :
        print ("I want to you put number bro!!")
        Numbermin ()

def Numbermax ():
    global max
    try :
        max = int(input("Enter number max : "))
    except :
        print ("I want to you put number bro!!")

def NumberRandom ():
    global NumberToGuess
    global min
    global max
    Numbermin ()
    Numbermax ()
    NumberToGuess = rd.randint(min,max)

def UserGuessNumber ():
    global Guess
    print ( f"<--- Welcome to guess game --->"  )
    Guess = int(input("How many time do you wanna guess : "))
    NumberRandom()
    GuessesNum()
    

def Rst ():
    restart = input("Another game? Answer yes or no : ").lower()
    if restart == "yes":
        UserGuessNumber ()
    elif restart == "no":
        sys.exit ("Thank you, I hope you fun the guess game")
    else :
        Rst()


def GuessesNum ():
    global Guess
    global UserGuess
    global NumberToGuess

    while UserGuess != NumberToGuess and Guess > 0 :
        Guess -= 1 
        try:
            UserGuess = int(input("If you sure number you put now : "))
        except :
            print (f"I want to you put number bro!!")
            GuessesNum ()
        if UserGuess > NumberToGuess :
            print (f"Too high! , Number of guess left : " +'[ ' + str(Guess) +' ]')
        elif UserGuess < NumberToGuess : 
            print (f"Too low!, Number of guess left : " + '[ ' + str(Guess) +' ]')
        elif UserGuess == NumberToGuess :
            print (f"Wow You won!!. Good Guess, You can take guess Exam : " + '[ ' + str(NumberToGuess) + ' ]')
            Rst()
    if UserGuess != NumberToGuess:
        print(f"Sorry!! you guess so bad, I think you should not guess the Exam : " + '[ '+  str(NumberToGuess) +  ' ]')
        Rst()


UserGuessNumber ()