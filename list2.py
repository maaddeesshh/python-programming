fruits = ["apple", "banana", "mango", "Potato", "beans"]
numbers = [1, 2, 3, 4, 5]
# fruits.append(numbers)
# print(fruits)

fruits.extend(numbers)
print(fruits)


print(len(fruits))

count= 0
for fruit in fruits:
    count +=1
print(count)    