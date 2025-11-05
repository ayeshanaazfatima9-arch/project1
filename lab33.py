# Correct number to guess
correct_number = 7

#Initialize the user's guess
guess = 0

#Keep asking the user to guess until they get it right
while guess != correct_number:
    guess= int(input("Guess the number betweem 1 and 10:"))

    print("Congratulations! you guessed the correct number.")