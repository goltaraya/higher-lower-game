# Higher Lower game
# Author >>> Yago Goltara
from game_data import data          # Imports game_data from data module
import logo                         # Imports logo module
import random                       # Imports random module
import time                         # Imports time module
import os                           # Imports os module

name = input("Welcome to the HigherLower game! First, type your name: ")        # Gets the user's name
input(f"Alright, {name}! Press 'ENTER' to start...")                            # Stops flag
time.sleep(0.25)                    
os.system('cls')

score = 0               # Starts a variable "score" with value 0

stop_flag = False       # While loop stop flag

while stop_flag != True:                # Starts the while loop
    print(logo.logo)                    # Prints out the game logo
    a_choice = random.choice(data)      # Chooses a character from game_data and stores it in "A" variable 
    b_choice = random.choice(data)      # Chooses a character from game_data and stores it in "B" variable
    
    if a_choice != b_choice:            # If A and B aren't the same:
        print(f"\n{a_choice['name']}, a {a_choice['description']} from {a_choice['country']}.")
        print(logo.vs)
        print(f"{b_choice['name']}, a {b_choice['description']} from {b_choice['country']}.")
       
        user_choice = input(f"Who has more followers? Type 'A' or 'B': ").lower()           # Gets the user's guess
        if user_choice == 'a':                                                              # If user's guess be "A"
            if a_choice['follower_count'] > b_choice['follower_count']:
                score += 1
                print("You're right!")
                time.sleep(1)
            else:
                stop_flag = True
                break

        elif user_choice == 'b':                                                            # If user's guess be "B"
            if b_choice['follower_count'] > a_choice['follower_count']:
                score += 1
                print("You're right!")
                time.sleep(1)
            else:
                stop_flag = True
                break
       
        else:                                                                               # If user's guess not be "A" or "B"
            print("Input a valid command.")
            time.sleep(1)
    os.system('cls')

print(f"\nI'm sorry but you guessed it wrong.\n{name}, your final score is {score}.")
input()