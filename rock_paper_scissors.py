from random import randint

# List of play options
choice = ['Rock', 'Paper', 'Scissors']

# Random play by computer
computer = choice[randint(0, 2)]

# Setting player to False before choice is made
player = False

while player == False:
    x = input("What is your choice of throw? Enter Rock , Paper or Scissors ")

    if x == computer:
        print('Tie!')
    elif x == 'Rock':
        print('Player Choice: Rock')
        if computer == 'Paper':
            print('You Lose!', computer, 'covers', x)
        else:
            print('Player Wins!', x, 'smashes', computer)
    elif x == 'Paper':
        print('Player Choice: Paper')
        if computer == 'Rock':
            print('Player Wins!', x, 'covers', computer)
        else:
            print('You Lose!', computer, 'cuts', x)
    elif x == 'Scissors':
        print('Player Choice: Scissors')
        if computer == 'Paper':
            print('Player Wins!', x, 'cuts', computer)
        else:
            print('You Lose!', computer, 'smashes', x)

    else:
        print("Sorry, incorrect selection, please try again.")
    # Ask to play again
    new_game = input("Would you like to play again? Enter 'y' or 'n' ")
    if new_game[0].lower() == 'y':
        player = False
        continue
    else:
        print("Thanks for playing!")
    break




