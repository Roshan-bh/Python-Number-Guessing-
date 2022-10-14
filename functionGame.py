import random
#importing the Mastermind class from gameContent Module.
from gameContent import Mastermind

# defining function as run() which can be used multiple times

def run(): 
    Mastermind.guessCode()
    Mastermind.guessFlagColor()
    Mastermind.result_helper()
    print("Are you wanna play again ?? (Y/N) ")
    global choice
    choice=input() 

# invoking display() method  outside run() only because user name input need to taken only once during whole playing.

Mastermind.disp()

# loop continue until player wants to terminate the game.
while(True):

# the main method to start the game invoking as a run()
    
    run()
   
    if(choice[0]=="Y" or choice[0]=="y" or choice[0]=="N" or choice[0]=="n"):
        if(choice[0]=="Y" or choice[0]=="y"):
        
            run()
            

        if(choice[0]=="N" or choice[0]=="n"):
            uc=input("To see final result type E: ")
            if(uc[0]=="E" or uc[0]=="e"):
                Mastermind.result()
                break
            
    else:
      break
    
#--The End--#