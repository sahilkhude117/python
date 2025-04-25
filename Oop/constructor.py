class Student:
    def __init__(self, name='unknown', roll_no=0):
        self.name = name
        self.roll_no = roll_no
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print("-------------------------")

# Default constructor
student1 = Student()
print("Using Default Constructor: ")
student1.display_info()

# Parameterized constructor
student2 = Student("Sahil", 101)
print("Using Parameterized Constructor:")
student2.display_info()
