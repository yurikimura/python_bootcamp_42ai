import random

target = random.randrange(1, 99)

while True:
    pred = input("What's your guess between 1 and 99?\n")
    try:
        pred = int(pred)

        if pred == target:
            print("Congratulations, you've got it!")
            break

        elif pred > target:
            print("Too high!")

        elif pred < target:
            print("Too low!")
    except:
        print("That's not a number.")
