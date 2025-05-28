def greet():
    print("Hello, Eugene!")
greet()


def greet():
    return "Hello, Eugene!"

print(greet())  # Output: Hello, Eugene!


def greet(name):
    return "Hello, "+ name

print(greet("Eugene"))  # Output: Hello, Eugene!


def greet_user(name):
    print("Hello, " + name + "!")
    
greet_user("Eugene")  # Output: Hello, Eugene!

def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(5, 3))

def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print("The sum is:", sum_result)


def cube():
    num = 2
    result = num*num*num
    return result
print(cube())

def cube(num):
    result = num*num*num
    return result
print(cube(3))


def cube(num):
    result = num*num*num
    return result

x = cube(7)
print(x)

def cube(num):
    return num*num*num

x = cube(7)
print(x)



    