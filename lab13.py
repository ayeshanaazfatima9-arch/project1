def greet(name):
    print("Hello", name + "! Welcome to Python Lab.")

# Function call
greet("Ayesha")

def add_numbers(a, b):
    return a + b

# Function call
result = add_numbers(5, 7)
print("Sum is:", result)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function call
num = 5
print("Factorial of", num, "is:", factorial(num))