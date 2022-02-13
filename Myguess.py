from ast import Global, While
from glob import glob
import random as rd
import sys



min = ""
max = ""
NumberToGuess = ""
UserGuess = -1
Guess = ""

class bcolors:
    RED = '\033[31m'
    Blue = '\033[34m'
    Green = '\033[32m'
    ENDC = '\033[0m'

    
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
    print (bcolors.RED + "<--- " + bcolors.ENDC + bcolors.Green + "Welcome to guess game" + bcolors.ENDC + bcolors.RED + " --->" + bcolors.ENDC)
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
            print ("I want to you put number bro!!")
            GuessesNum ()

        if UserGuess > NumberToGuess :
            if Guess == 0:
                print ("Too high! , Number of guess left : " +'[ ' + bcolors.RED + str(Guess) + bcolors.ENDC +' ]')
            else:
                print ("Too high! , Number of guess left : " +'[ ' + bcolors.Blue + str(Guess) + bcolors.ENDC +' ]')
        elif UserGuess < NumberToGuess :
            
            if Guess == 0 :
                print ("Too low!, Number of guess left : " + '[ ' + bcolors.RED + str(Guess) + bcolors.ENDC +' ]')
            else:
                print ("Too low!, Number of guess left : " + '[ ' + bcolors.Blue + str(Guess) + bcolors.ENDC +' ]')
        elif UserGuess == NumberToGuess :
            print ("Wow You won!!. Good Guess, You can take guess Exam : " + '[ ' + bcolors.Green + str(NumberToGuess) + bcolors.ENDC + ' ]')
            Rst()
    if UserGuess != NumberToGuess:
        print("Sorry!! you guess so bad, I think you should not guess the Exam : " + '[ '+ bcolors.Green + str(NumberToGuess) + bcolors.ENDC + ' ]')
        Rst()


UserGuessNumber ()

