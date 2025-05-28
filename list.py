fruits = ["apple", "banana", "mango", "Potato", "beans"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 99, True]
print(fruits,  numbers, mixed)
print(fruits[0])  # apple
print(fruits[2])  # mango
print(fruits[-1])
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'mango']
print(fruits[1:]) # grabs list items from position 1 onwards
print(fruits[1:4]) # grabs list items from position 1 upto but not including 4
fruits.extend(numbers)   # adds another list 
print(fruits)

# Add to end
fruits.append("orange")
print(fruits)
# Insert at position
fruits.insert(1, "grape")
print(fruits)

# Remove by value
fruits.remove("mango")
print(fruits)

# Remove by index
# del fruits[0]

# # Clear everything
# fruits.clear()

fruits.pop()  # pop out the last element in a list
print(fruits)
print(fruits.index("apple"))

numbers = [1, 2, 3, 2, 4, 2, 5]
print(numbers.count(2))  # Output: 3

nums = [3, 1, 4, 2]
nums.sort()
print(nums)  # Output: [1, 2, 3, 4]

words = ["banana", "apple", "cherry"]
words.sort()
print(words)  # Output: ['apple', 'banana', 'cherry']


numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

original = [1, 2, 3]
copy_list = original.copy()

print("Original:", original)      # Output: [1, 2, 3]
print("Copied:", copy_list)       # Output: [1, 2, 3]

original_list = [1, 2, 2, 3, 4, 3, 5, 1]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", original_list)
print("Without duplicates:", unique_list)

original_list = [1, 2, 2, 3, 4, 3, 5, 1]
unique_list = list(set(original_list))
print(unique_list)  # Might not maintain the order


numbers = [5, 12, 3, 21, 7, 9]

max_value = max(numbers)

print("The maximum value is:", max_value)

numbers = [5, 12, 3, 21, 7, 9]
max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print("The maximum value is:", max_value)


original_list = [1, 2, 2, 3, 4, 3, 5, 1]
unique_list = []
duplicate_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
    else:
        duplicate_list.append(item)

print("Original list:", original_list)
print("Without duplicates:", unique_list)
print("Duplicates:", duplicate_list)


