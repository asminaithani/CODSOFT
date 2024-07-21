import random

choices = ("rock", "paper", "scissors")

running = True

while running:

  computer = random.choice(choices)
  user = None

  while user not in choices:
    user = input("Enter a choice (rock, paper, scissors): ")

    print(f"Computer: {computer}")
    print(f"Player: {user}")

    if user == computer:
      print("It's a tie")

    elif user=="rock" and computer == "scissors":
      print("You win")

    elif user =="paper" and computer =="rock":
      print("You win")

    elif user =="scissors" and computer =="paper":
      print("You win")

    else:
       print("You lose")

    play_again = input("Play again? (y/n)").lower() 
    if  play_again == "y":
      running = True
    elif play_again == "n":
      running = False
    else:
      print("Please enter a valid option (y/n)")
      
print("Thanks for playing")