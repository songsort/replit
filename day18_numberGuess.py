print("One-Million-To-One")

number = 500
count = 0

while True:
  count = count + 1
  gues = float(input("What is your guess? "))
  guess = int(gues)
  if guess < 0:
    break 
  if guess > number:
    print("Too high")
  elif guess < number:
    print("Too low")
  else:
    print("Correct")
    print("It took you ", count, "guesses")
    break
    # exit()