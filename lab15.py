# Write mode: creates file if not exists
with open("sample.txt", "w") as file:
    file.write("Edunet is awesome!\n")
    file.write("Python makes file handling easy.\n")

    # Read mode
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Append mode
with open("sample.txt", "a") as file:
    file.write("This line is added later.\n") 
with open("sample.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())