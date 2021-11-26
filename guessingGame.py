import random
print(random.randint(0,9))

guess = int(input("Enter your guess"))
chances = 0
number = random.randint(0,9)

while chances < 5:
    if guess == number:
        print("Congratulations YOU WON!!")
        break

    if not chances <5:
        print ("YOU LOSE!! The number is", number)
