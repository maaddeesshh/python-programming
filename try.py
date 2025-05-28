# try:
#     number = int(input("Enter a number: "))
#     print("You entered:", number)
# except:
#     print("Oops! That wasn't a valid number.")



# try:
#     num= 10/0
#     number = int(input("Enter a number: "))
#     print("You entered:", number)
# except ZeroDivisionError as err:
#     print(err)    
# except ValueError:
#     print("Oops! That wasn't a valid number.")




# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print("Result is:", result)
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")


# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
# except (ValueError, ZeroDivisionError) as e:
#     print("An error occurred:", e)
# else:
#     print("Result is:", result)
# finally:
#     print("This runs no matter what.")


try:
    num1 = int(input("enter number: "))
    result1 = num1 + 5
    print(result1)
except:
    print("Invalid input")     