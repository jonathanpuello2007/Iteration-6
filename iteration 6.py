import random

print("Let's play rock, paper, scissors")


def get_user_choice():
  while True:
    try:
      choice = input("Choose rock, paper, or scissors: ")
      if choice not in ["rock", "paper", "scissors"]:
       raise ValueError
    except ValueError:
      print("Please enter 'rock', 'paper', 'scissors'.")
    else:
      return choice

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  cpu_choice = random.choice(choices)
  return cpu_choice

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print("IT'S A TIE!")

  elif (user_choice == "scissors" and computer_choice == "paper") or \
  (user_choice == "paper" and computer_choice == "rock") or \
  (user_choice =="rock" and computer_choice=="scissors"):
    print("You won")
    
  else:
    print("THE COMPUTER WINS")

def play_game():
  while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"The computer chose: {computer_choice}")
    determine_winner(user_choice, computer_choice)
    choice = input("Do you want to play again (y/n)?: ")
    if choice == "y":
      
        continue
    if user_choice == "n":
      
        print("Invalid input. Please check what is wrong.")
      
    else:
        break

  

play_game()
