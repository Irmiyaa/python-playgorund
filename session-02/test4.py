import random

label = ("Easy, Normal, Hard")
print(label)
difficult = input("Select Your Difficult :")
number = 1

if difficult == "Easy":
    number = 10
elif difficult == "Normal":
    number = 100
elif difficult == "Hard":
    number = 1000
else :
    print("Input Not Valid")

secret_number = random.randint(1, number)
guess = 0

print("╔══════════════════════════╗")
print("     GUESS THE NUMBER")
print("╚══════════════════════════╝")
print("I'm thingking of a number between 1 and ", number)

while guess != secret_number:
    guess = int(input("Your guess :"))

    if guess > 100:
        print("Your guess bigger 100")
    elif guess > secret_number:
        print("Too high! Try again")
    elif guess < secret_number:
        print("Too low! Try again")
    else:
        print("🎉 CORRECT!")