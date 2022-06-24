import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# List that contains all the options
options =[rock,paper,scissors]


while True:
  # Take input from user and print their choice
    user_choice= options[int(input('Type 0 for Rock, 1 for Paper, and 2 for Scissors\n'))]
    print("You chose:\n",user_choice)
    # Take a random guess for the computer
    computer_choice = random.choice(options)
    print("Computer chose:\n",computer_choice)
    if user_choice == computer_choice:# If it is a tie, take the input again
        print("It's a TIE! Choose again")
        continue
    elif user_choice != computer_choice:# If not a tie, check only for the losing conditions
      if (user_choice == rock and computer_choice== paper) or (user_choice == paper and computer_choice == scissors) or (user_choice == scissors and computer_choice == rock):
          print('Sorry you LOSE!!!')
          inp=input("Play again? Enter 'y' for yes and 'n' for no\n")# Take input from the user whether or not they want to play again.
          if inp.lower() == 'y':# If they want to play again, then continue the game from the beginning of the while loop.
              continue
          else:# If they don't want to play, then break out of the while loop and end the game.
              break
      else:
          print("Congrats you WIN!!!")
          inp=input("Play again? Enter 'y' for yes and 'n' for no\n")
          if inp.lower() == 'y':# If they want to play again, then continue the game from the beginning of the while loop.
              continue
          else:# If they don't want to play, then break out of the while loop and end the game.
              break 




   


  

