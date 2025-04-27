import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK: 'rock', PAPER: 'paper' , SCISSORS: 'scissors '}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissors? (r/ p/ s): ').lower()
        if user_choice  in  choices: # != ROCK and user_choice != PAPER and user_choice !=SCISSORS:
           return user_choice
        else:
         print('Invalid choice!')


def display_choices (user_choice, computer_choice):
    print(f'you choose {emojis[user_choice]}') #or use canc + user_choice )
    print(f'computer choose {emojis[computer_choice]}')


def determin_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 's' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r' )):
        print('you win')
    else:
        print('you lose ')
 

def paly_game():
        while True:
            user_choice = get_user_choice()

            
            computer_choice = random.choice(choices)       
            

        
            display_choices(user_choice,computer_choice )

            determin_winner(user_choice,computer_choice)
    
        

            should_continue = input('continue? (y/n):  ').lower()
            if should_continue == 'n':
                break

paly_game()

# a dictionary is used in python to mrk a key to a value 
# key ->  value 
# "r"  to  Rock
# "s"  to  scissors 
# "p"  to  paper 

#Dry in programming means dont repeat your self 
