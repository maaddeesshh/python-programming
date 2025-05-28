class Student:
    def __init__(self, name, age):
        self.name = name    # Assign parameter 'name' to this object's 'name' property
        self.age = age      # Assign parameter 'age' to this object's 'age' property

    def greet(self):
        print("Hello, my name is " + self.name)

# Create two students
student1 = Student("Eugene", 17)
student2 = Student("Max", 18)
student3 = Student("Omollo", 19)

# Call greet() for each student
student1.greet()  # Output: Hello, my name is Eugene
student2.greet()  # Output: Hello, my name is Max
student3.greet()  # Output: Hello, my name is Max
