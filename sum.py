# def sum_of_digits(number):
#     # Convert number to string to iterate through its digits
#     num_str = str(number)
#     # Initialize sum
#     digit_sum = 0
#     # Iterate through each digit and add it to the sum
#     for digit in num_str:
#         digit_sum += int(digit)
#     return digit_sum

# # Example usage
# input_number = 12345
# result = sum_of_digits(input_number)
# print("Sum of digits in", input_number, "is", result)




# def sum_of_digits(number):
#     # Convert number to string to iterate through its digits
#     num_str = list(str(number))
#     # Initialize sum
#     digit_sum = 0
#     # Iterate through each digit and add it to the sum
#     for digit in num_str:
#         digit_sum += int(digit)
#     return digit_sum

# # Example usage
# input_number = 12345
# result = sum_of_digits(input_number)
# print("Sum of digits in", input_number, "is", result)



# def sum_of_digits(number):
#     # Convert number to string to iterate through its digits
#     num_str = number
#     # Initialize sum
#     digit_sum = 0
#     # Iterate through each digit and add it to the sum
#     for digit in num_str:
#         digit_sum += int(digit)
#     return digit_sum

# # Example usage
# input_number = input("Enter number: ")
# result = sum_of_digits(input_number)
# print("Sum of digits in", input_number, "is", result)




def sum_of_digits(number):
    # Convert number to string to iterate through its digits
    num_str = number
    # Initialize sum
    digit_sum = 0
    # Iterate through each digit and add it to the sum
    for digit in num_str:
        digit_sum += digit
    return digit_sum

# Example usage
input_number = [12,13,14,15]
result = sum_of_digits(input_number)
print("Sum of digits in", input_number, "is", result)



def find_average(numbers):
    if not numbers:  # If the list is empty
        return None  # Return None since there are no numbers to average
    total = sum(numbers)  # Calculate the sum of numbers in the list
    average = total / len(numbers)  # Calculate the average
    return average

# Example usage
number_list = [10, 20, 30, 40, 50]
average = find_average(number_list)
if average is not None:
    print("Average of numbers in the list:", average)
else:
    print("The list is empty.")



def find_average(numbers):
    if not numbers:  # If the list is empty
        return None  # Return None since there are no numbers to average
    total = 0 # Calculate the sum of numbers in the list
    for num in numbers:
        total += num
    average = total / len(numbers)  # Calculate the average
    return average

# Example usage
number_list = [10, 20, 30, 40, 50]
average = find_average(number_list)
if average is not None:
    print("Average of numbers in the list:", average)
else:
    print("The list is empty.")
