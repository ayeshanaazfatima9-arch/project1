# Start at 10
number = 10

# Decrement the number until it reaches 5, then break the loop
while number > 0:
    print(number)
    number -= 1
    if number == 5:
        break

    print("loop terminated early because the number reached 5.")