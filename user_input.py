name = input("Enter your name: ")   # Prompts the user and stores input as a string
age = input("Enter your age: ")
print("Hello " + name + " you are " + age + " years old")               # Prints a greeting with the user's name

# Basic calculator with two inputs and one result variable

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Arithmetic operations
result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2  # Note: No check for division by zero

# Results
print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)
print("Division:", result_div)


# Get input as string (default behavior)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Perform conversion at the time of calculation
result = float(num1) + float(num2)

# Print the result
print("The result is:", result)


# Get input as string (default behavior)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Perform conversion at the time of calculation
result = int(num1) + int(num2)

# Print the result
print("The result is:", result)


