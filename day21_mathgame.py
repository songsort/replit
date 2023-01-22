print("Math Game!")
print()
multiples = int(input("Name your multiples: "))
correctAnswer = 0

for i in range(1, 11):
    print(i, "x", multiples, "=")
    answer = int(input(""))
    if answer == i * multiples:
        print("Great work! ")
        print()
        correctAnswer += 1
    else:
        print("Nope! The answer was", i * multiples)
        print()
if correctAnswer == 10:
  print("Wow! Aperfect score!")
else:
  print("You score", correctAnswer, "out of 10.")

