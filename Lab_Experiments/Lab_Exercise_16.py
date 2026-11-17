import random

while True:
    n = int(input("Enter number of dice to roll: "))
    for i in range(n):
        print("Dice", i + 1, ":", random.randint(1, 6))
    choice = input("Roll again? (yes/no): ")
    if choice.lower() != "yes":
        break
