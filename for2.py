# def trial(x,y):
#     result = 1
#     for index in range(y):
#         result = result * x
#     return result       



# print(trial(3,4)) 




def trial(x,y):
    result = 1
    for index in range(y):
        result = result * x
        # return result
    return result       

num1 = float(input("Enter number: "))
num2 = int(input("Enter another number: "))

print(trial(num1, num2)) 