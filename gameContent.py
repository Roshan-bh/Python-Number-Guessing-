import random

#declaring class as Mastermind.

class Mastermind():
    global  Maximum_Number_Guesses,Number_of_Digits,correct,count
    Maximum_Number_Guesses=1
    Number_of_Digits=3
   
   
 #--display() function to display the some instructions about game. 

    def disp():
            #--Introduction About Game--#
        print("       ~~~~~~Welcome to the Mastermind Game~~~~~    ")
        print("Hi gamer, welcome to the Mastermind game")
        name=input("What is your name? ")
        print(f"Hello, {name}, Please follow the given instructions to play the game.")
        print()
        print("       ~~~~~~GAME INSTRUCTION~~~~~    ")
        print('''I am thinking of a 3-digit number. Try to guess what it is.
        Here are some clues:
        When I say:         That means:
        Yellow              One digit is correct but in the wrong position.
        Green               One digit is correct and in the right position.
        Red                 No digit is correct.

        For example, if the secret number was 346 and your guess was 843, the clues
        would be hint:Green
                hint:Yellow.
        ''')

#--guessCode(.......) which will Returns a string made up of number_of_digits (3) unique random digits. 
     
    def guessCode():

        print("Game is to guess integer number of 3 digits")
        list1=["0","1","2","3","4","5","6","7","8","9"]
        global random_number

#--generating random number from the aboove list1 through string concanating.

        random_number=(random.choice(list1))+(random.choice(list1))+(random.choice(list1))

#-- printing the randomly generated number for debug purpose--#
        # print(random_number)

#--declaring random_number_list variable as a global to be accessed from the others function.

        global random_number_list
        random_number_list=list(random_number)
     
    
#--guessFlagColor(.......) which will return a string with the yellow, green, red clues for a guess andsecret number.
   
    def guessFlagColor():
          
            
           
            i=0
        
            while(i< Maximum_Number_Guesses):

                #--declaring str_guess variable as a global to be accessed from the others function.

                global str_guess

                guess=int(input("Enter the three digit integer number to guess : "))
    
                str_guess=str(guess)
    
                list_guess=list(str_guess)

                # checking if the length of the guess number is with 3 digits or not.

                while(len(list_guess)==Number_of_Digits):

                # comparing two strings.

                    if( str_guess!=random_number):
                          
                            print("Opps!! Sorry but you can  get it through hint: ")
                
                            for n in list_guess:
                        
                                if(n not in random_number_list):
                        
                                    print("hint: Red")
                                    

                                if(n in random_number_list and list_guess.index(n)!=random_number_list.index(n) ):
                                    print("hint: Yellow")
                                    

                                if(n in random_number_list and list_guess.index(n)==random_number_list.index(n) ):
                                    print("hint: Green")

                    if( str_guess != random_number and i==(Maximum_Number_Guesses-1)):
                        
                        print(f" Sorry !! Your chances are over the actual number is {random_number} ")
                        
                    if(str_guess==random_number):
                    
                        print(f"Yes!! You Guess Correct Number which is {random_number} ")
                        print("Thanks for Participation!!")
                        break
                    break
#  start while loop increment.
                i=i+1
            
# declaring some global variable as 0 for counting purpose.
           
    correct=0  
    count=0  
# result helper method named as result_helper() to produce result.
    def result_helper():
            global correct
            global count
            count=count+1
            if(str_guess==random_number):
                    
                     correct=correct+1
                     return correct

# dispResult(...... ) which will display game results. At the end of the log you should print a summary:
# About the series of games played by the user,these being the total number of games played
#The total number of guesses made (use another variable to keep track of this)
#The average number of guesses per game.
    
    def result():

         print(f"Total times you played : {count}") 
         print(f"Total times you guessed correct : {correct}")
         print(f"The average number of guesses per game : {correct/count}")



        


            
            
           
        
       
             


        

                

