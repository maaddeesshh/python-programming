age = 2

if age >= 18:
    print("You are an adult.")
else:
    print("YOU ARE YOUNG")
    
    
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
    
    
is_raining = True

if is_raining:
    print("Take an umbrella.")
else:
    print("Enjoy the sunshine!")

is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("Welcome, Admin!")
else:
    print("Access denied or limited access.")


is_logged_in = False
is_admin = False

if is_logged_in or is_admin:
    print("You can proceed.")
else:
    print("Access denied.")


# Define boolean variables
has_access = True   # Change to False to test other conditions
is_admin = False    # Change to True to test the admin condition

# Check the conditions using if, elif
if has_access and is_admin:
    print("You are an admin and you can proceed.")
elif has_access and not is_admin:
    print("You have access, but you are not an admin.")
elif not has_access and is_admin:
    print("You are an admin, but access is denied.")
else:
    print("Access denied.")



def get_max_value(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Get user input for the three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Call the function with the user inputs
result = get_max_value(a, b, c)
print("The maximum value is:", result)


# Simple Calculator using if and elif

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose the operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user's choice
choice = input("Enter the number of the operation (1/2/3/4): ")

# Perform operation using if and elif
if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice.")

    
    
    
num3 = float(input("Enter num: "))
num4 = float(input("Enter another number: "))
op = input("Enter operator(+,-,/,%,*): ")

if op == '+':
    Result= num3 + num4
    print("Result is " + str(Result))
elif op == '-':
    Result = num3-num4
    print("Result is " + str(Result))
elif op == '/':
    if num4 != 0:
        Result = num3/num4
        print("Result is " + str(Result))  
    else:
        print("Error: Cannot divide by zero.")
elif op == '*':
    Result = num3*num4
    print("Result is " + str(Result)) 
elif op == '%':
    Result = num3%num4
    print("Result is " + str(Result)) 
else:
    print("Invalid operator choice.")
                  
        
                      