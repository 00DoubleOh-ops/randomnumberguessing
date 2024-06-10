import random

com_num = random.randint(1,100)

print(f"{com_num}")

while True:
    try:

        player_guess = int(input("Enter your guess: "))
        if player_guess == com_num:
            print("Congratulations, you guessed right!")
            break
        elif player_guess < com_num:
            print("Number is too low!")
        elif player_guess > com_num:
            print("Number is too high!")
    except ValueError:
        print("Invalid entry.")
