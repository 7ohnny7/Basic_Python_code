# Creating a Student and Course Class + Defining attrubutes and methods.
# Defined a Class and set attributes.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100%
      
# Defined a method to get grade.

    def get_grade(self):
        return self.grade

# Defined a Class for student courses and its attributes.
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
# Defined a method to add students to a list.

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

# Defined a method to get the average grade of the students.
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

# Added Students using parameters "name", "age", and "grade". (add more students if req.).
s1 = Student("Jonny", 24, 89)
s2 = Student("Joe", 47, 78)
s3 = Student("Jane", 35, 81)
s4 = Student("Jess", 31, 90)

# Added Course and how many students per course. (add more if req.).
course = Course("Computer_science" , 30)

# Added students to course.
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)

# Output data using pring function.
print(course.add_student(s1))
print(course.add_student(s2))
print(course.add_student(s3))
print(course.add_student(s4))
print("Course:", course.name)
print("Average grade:", course.get_average_grade())
print("Max students per class:", course.max_students)

