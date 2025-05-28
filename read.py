employee_file= open("employees.txt",  "r")
print(employee_file.readable())    #checks if the file is readable boolean value is returned
print(employee_file.read())  #spits out contents of the file
# print(employee_file.readline()) #first line read
# print(employee_file.readline())# second line read and so on
print(employee_file.readlines()) #reads the entire line of the file
# print(employee_file.readlines()[3]) 



for employee in employee_file.readlines():
    print(employee)

employee_file.close()





# read(r),write(w), append(a), read and write(r+)--  modes