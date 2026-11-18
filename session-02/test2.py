import random

secret_number = random.randint(1, 100)
guess = int(input("Masukkan nomer tebakan anda :"))

if guess > 100 :
    print("angka lebih dari 100")
elif guess > secret_number:
    print("Too high!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Correct!")

print("angka yang benar adalah :", secret_number)