import random

def dice_game():

    #code for the first round of the game
    
    print("Score 24 or more with 3 rolls of 2 dice to win!")
    print("Ready to roll the dice?")
    input("Press Enter to continue...")

    total = 0
    score = 0

    dice1 = random.randrange(1,6)
    dice2 = random.randrange(1,6)

    score = dice1 + dice2
    total += score

    print("You scored %d this round!"%(score))
    print("Ready to roll the dice again?")
    input("Press Enter to continue...")

    #code for the second round of the game

    dice1 = random.randrange(1,6)
    dice2 = random.randrange(1,6)

    score = dice1 + dice2
    total += score

    if total >= 24:
        
        print("Congratulations! You won the game with a score of %d"%(total))
        print("Do you want to play again?")
        input("Press Enter to continue...")
    else:

        print("You scored %d this round, and your total is now %d!"%(score,total))
        print("Ready to roll the dice again?")
        input("Press Enter to continue...")

        #code for the final round

        dice1 = random.randrange(1,6)
        dice2 = random.randrange(1,6)
        
        score = dice1 + dice2
        total += score

        if total >= 24:
            
            print("Congratulations! You won the game with a score of %d!"%(total))
            print("Do you want to play again?")
            input("Press Enter to continue...")
            dice_game()

        else:

            print("Unlucky, you scored %d this round, giving you a final total of %d."%(score,total))
            print("Do you want to play again?")
            input("Press Enter to continue...")
            dice_game()


dice_game()