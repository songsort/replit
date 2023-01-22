while True:
    print("You are in a corridor, do you go left or right ?")
    direction = input("> ")
    if direction == "left":
        print("You have fallen to your death!")
        break
    elif direction == "right":
        print("good move")
        continue
    else:
        print("Ahh! You are a genius, you've won.")
        exit()
    print("Game over, you have failed!")