print()
print("EPIC ROCK PAPER SISSOR BATTLE")
name1 = input("What's Player 1 name? ")
name2 = input("What's Player 2 name? ")
print()
from getpass import getpass as input
player_1Move = input(f"Select your move {name1} (R, P or S) ")
player_2Move = input(f"Select your move {name2} (R, P or S) ")
print(name1 +"'s move:", player_1Move, ";", name2 +"'s move:", player_2Move)
if (player_1Move == "R" or player_1Move == "S" or player_1Move == "P") and (player_2Move == "R" or player_2Move == "S" or player_2Move == "P"):
  if player_1Move == "R":
    if player_2Move == "R":
      print("Rock hits rock - draws")
    elif player_2Move == "P":
      print("Paper wraps rock,", name2, "wins")
    elif player_2Move == "S":
      print("Rock breaks scissors,", name1, "wins")
  if player_1Move == "P":
    if player_2Move == "R":
      print("Paper wraps rock,", name1, "wins")
    elif player_2Move == "P":
      print("Paper wraps paper, - draws")
    elif player_2Move == "S":
      print("Scissors cut paper,", name2, "wins")
  if player_1Move == "S":
    if player_2Move == "R":
      print("Rock breaks scissors,", name2, "wins")
    elif player_2Move == "P":
      print("Scissors cut paper,", name1, "wins")
    elif player_2Move == "S":
      print("Scissors draws scissors")
else:
  print("wrong move")