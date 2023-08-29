#import the random method from the randint module
from random import randint

# Define the roles 
roles = ["Bear", "Ninja", "Cowboy"]

#generate a raondom role using an array
computer = roles[randint(0,2)]

player = False

while player == False:
#get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    if computer == player:
        print("DRAW")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", computer, "shoots", player)
        else: #computer is cowboy, player is ninja
            print("You win!", player, "defeats", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print ("You win!", player, "shoots", computer)
        else:
            print("You lose!",player, "is eaten by", computer)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", player, "is defeated by", computer)
    else: # computer is ninja, player is bear
            print("You win!", player, "eats", computer)

#after checking who won, put the following code
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
        player = False
        computer = roles[randint(0,2)]
    else:
        break
  
 
