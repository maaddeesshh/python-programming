def reverse_string(input_string):
    reversed_string = ''
    for char in input_string:
        reversed_string = char + reversed_string 
    return reversed_string


input_string = input("Enter a string to reverse: ")
# reversed_string = reverse_string(input_string)
# print("Reversed string: " + reversed_string)
print(reverse_string(input_string))


# input_string= input("Enter a word: ")
# reverse_string = ''
# for char in input_string:
#     reverse_string = char + reverse_string
 
# print(reverse_string)    
