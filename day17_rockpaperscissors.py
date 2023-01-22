print()
print("EPIC ROCK PAPER SISSOR BATTLE")
name1 = input("What's Player 1 name? ")
name2 = input("What's Player 2 name? ")

player1Score = 0
player2Score = 0
print()
    
from getpass import getpass as input

while True:

    player_1Move = input(f"Select your move {name1} (R, P or S) ")
    player_2Move = input(f"Select your move {name2} (R, P or S) ")
    print(name1 +"'s move:", player_1Move, ";", name2 +"'s move:", player_2Move)
    if (player_1Move == "R" or player_1Move == "S" or player_1Move == "P") and (player_2Move == "R" or player_2Move == "S" or player_2Move == "P"): # avoid wrong move
        if player_1Move == "R":
            if player_2Move == "R":
                print("Rock hits rock - draws")
            elif player_2Move == "P":
                print("Paper wraps rock,", name2, "wins")
                player2Score = player2Score + 1
            elif player_2Move == "S":
                print("Rock breaks scissors,", name1, "wins")
                player1Score = player1Score + 1
        if player_1Move == "P":
            if player_2Move == "R":
                print("Paper wraps rock,", name1, "wins")
                player1Score = player1Score + 1
            elif player_2Move == "P":
                print("Paper wraps paper, - draws")
            elif player_2Move == "S":
                print("Scissors cut paper,", name2, "wins")
                player2Score = player2Score + 1
        if player_1Move == "S":
            if player_2Move == "R":
                print("Rock breaks scissors,", name2, "wins")
                player2Score = player2Score + 1
            elif player_2Move == "P":
                print("Scissors cut paper,", name1, "wins")
                player1Score = player1Score + 1
            elif player_2Move == "S":
                print("Scissors draws scissors")
    else:
        print("wrong move") # line 17
    if player1Score == 3 or player2Score == 3:
        break
    
print(name1, "score is", str(player1Score) +";", name2, "score is", player2Score)

if player1Score > player2Score:
    print("Congratulations to", name1, "you won the game!")
else:
    print("Congratulatons to", name2, "you won the game!")