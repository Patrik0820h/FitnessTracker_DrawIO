import random

secret_number = random.randint(0,11)
work = True

print("Welcome to Akinator. You need to guess the number between 0-10 that the engine selects! Good luck!")
print("\n")

def game():
    while(True):
        guess = int(input("Enter a guess: "))
        if guess > secret_number:
            print("Lower!")
            guess = int(input("Enter a guess: "))
        if guess < secret_number:
            print("Higher!")
            guess = int(input("Enter a guess: "))
        else:
            print("You have guessed the number!")
            replay = input("Would you like to replay? (Y/N): ").lower()
            if(replay == "y"):
                game()
            else:
                break
game()