#rock-paper-scissors

import random
action_list=['rock','paper','scissors']

computer_score = 0
player_score = 0

total_rounds = input ("how many rounds do you want to play?") 

round_counter=0

while True:
  round_counter+=1
  print("Round number:", round_counter)

  #select a random action for computer
  computer_choice=random.choice(action_list)

  player_choice=input("Please choose your action: ")

  print("Comnputer:", computer_choice)
  print("Player:", player_choice)

  if computer_choice==player_choice:
    print("Tie! Both players chose the same action")

  elif computer_choice=='paper':
    if player_choice=='rock':
      print("Computer is winner")
      computer_score+=1
    else:
      print("Player is winner") 
      player_score+=1

  elif computer_choice=='rock':
    if player_choice=='scissors':
      print("computer is winner")
      computer_score+=1
    else:
      print("Player is winner")   
      player_score+=1
  elif computer_choice=='scissors':
    if player_choice=='paper':
      print("Computer is winner")
      computer_score+=1
    else:
      print("Player is winner")  
      player_score+=1



  if round_counter==int(total_rounds):
    break

if computer_score==player_score:
  print ("There is no winner. Tie")

elif computer_score>player_score:
  print("Computer won") 

else:
  print("player won")
