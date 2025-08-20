# program of guessing the random number given by computer

import random 
def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    
    while guess != rand_num:
        guess= int(input(f"Enter the guess number between 1 to {x}:- "))
        if guess > rand_num:
            print("Sorry guess again its too high !")
        elif guess < rand_num:
            print("Sorry guess again its too low !")
    
    if guess == rand_num:
        print(f"Yay you gussed the correct number {rand_num}\nCongrats 👏")


guess(10) 

# program to guess the number given by you 
import random 
def computer(x):
    
    high = x
    low = 1
    feedback = ""
    num = int(input("Enter the number that you select:- "))
    print(f"Computer will guess {num} !")
    
    while feedback != "c":
       guess = random.randint(low,high)
       
       feedback = input(f"Is {guess} is too high 'H' , too low 'L' , correct 'C':- ").lower()
       if feedback == 'h':
           high = guess - 1
       elif feedback == 'l':
            low = guess - 1
            
    print("Computer Guessed our number corretly 👏 !")

computer(100)

#program to guess number by only with loop not with function 
import random 
n = int(input("Enter the range:- "))
computer = random.randint(1,n)
while True:
        

        guess = input(f'guess the number between 1 to {n} or type Q for quite:- ')
        if(guess.lower() == 'q'):
            print("Exit")
            break
        guess = int(guess)
    
        if(computer == guess):
            print("Wow you guessed the number !")
            break
        elif(guess > computer):
            print("its too high !")
        elif(guess < computer):
            print("Its too low !")
