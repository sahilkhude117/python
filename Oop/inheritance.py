class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return super().__str__() + f', Student ID: {self.student_id}'
    
class CollegeStudent(Student):
    def __init__(self, name, age, student_id, college_name):
        super().__init__(name, age, student_id)
        self.college_name = college_name

    def __str__(self):
        return super().__str__() + f'College: {self.college_name}'
    
if __name__ == '__main__':
    print("\n---Single Level Inheritanxe Demo---")
    student1 = Student("Sahil", 20, "ST101")
    print(student1)

    print("\n--- Multiplevel Inheritance---")
    college_student1 = CollegeStudent("Aditya", 21, "ST202", "XYZ Institute of Tech")
    print(college_student1)