class Person:
    def __init__(self,name, id_number):
        self.name = name
        self.id_number = id_number
        
    def _str_(self):
        return f'Name:{self.name}, ID: {self.id_number}'


class Student(Person):
    def __init__(self, name, id_number, major):
          super().__init__(name, id_number)
          self.major = major
         
    def __str__ (self):
        return f'Major:{self.major}, Name:{self.name}, ID: {self.id_number}'   
    
    
class Instructor(Person):
    def __init__(self, name, id_number,department):
        super().__init__(name, id_number)
        self.department = department

    def __str__ (self):
        return f'Department:{self.department}, Name:{self.name}, ID: {self.id_number}'
        
class Course:
    def __init__(self, course_name, course_id):

        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []
    
    def add_student(self, student):
        self.enrolled_students.append(str(student))

    def remove_student(self, student):
        self.enrolled_students.remove(str(student))

    def __str__(self):
        return f'Course: {self.course_name} (ID: {self.course_id})'
    
class Enrollment:
    def __init__(self, student, course, grade=None):

        self.student = student
        self.course = course
        self.grade = grade

    def assign_grade(self, grade):
        self.grade = grade
        
    def __str__(self):
         return f'Enrollment [Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}]'

class StudentManagementSystem:
    def __init__(self):

        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student):
        self.students.append(str(student))
        
    def remove_student(self, student):
        self.students.remove(str(student))
        
    def add_instructor(self, instructor):
        self.instructors.append(str(instructor))

    def remove_instructor(self, instructor):
        self.instructors.remove(str(instructor))

    def add_course(self, course):
        self.courses.append(str(course))

    def remove_course(self, course):
        self.courses.remove(str(course))
    
    def enroll_student(self, course, grade, student):
        self.enrollments.append(str(Enrollment(student, course, grade)))
        course.add_student(str(student))