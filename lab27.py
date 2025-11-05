# A string
word = "Edunet Foundation"

# Using a for loop to iterate over each character
for letter in word:
    print (letter)

    # Task 2 : using range to iterate from 0 to 4
    for i in range(0,5):   # range(5) also works, it means 0 to 4
        print(i)

        # Number of row for the triangle
        rows = 5

        #outer loop for the number of rows
        for i in range(1, rows + 1):
            #Inner loop for printing asterisks in each row
            for j in range(i):
                print("*", end=" ") #print an asterisk followed by a space
                Print:() # ove to the next line after finishing the inner loop