import random
print("\tWelcome to 'guess my number'!")
print("\nI'm thinking of a number between 1 and 100")
print("Try to guess it in 5 guesses.")

the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    tries += 1
    if tries >= 5:
        print("\nYou are out of tries!")
        exit()

print("you guessed it! The number was", the_number)