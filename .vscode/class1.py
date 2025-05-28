class Student:
    def __init__(self, name, age, grade):
        self.name = name        # instance variable
        self.age = age
        self.grade = grade

    def get_info(self):
        return self.name + " is " + str(self.age) + " years old and in grade " + str(self.grade) + "."

Student1 = Student("Eugene", 17, 9)

print(Student1.get_info())
# print(Student1.name)




