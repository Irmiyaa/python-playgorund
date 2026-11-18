secret_number = 37
guess = 0

while guess != secret_number:
    guess = int(input("Your guess :"))

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct")