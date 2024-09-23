from school_management import *
def main():
    # Create the system
    sms = StudentManagementSystem()

    # Create some students and instructors directly using the Student and Instructor classes
    student1 = Student("James Pan", 1, "Computer Science")
    student2 = Student("Ken Smith", 2, "Mathematics")
    instructor1 = Instructor("Dr. Peter", 101, "Engineering")

    # Add students and instructors to the system
    sms.add_student(student1)
    sms.add_student(student2)
    sms.add_instructor(instructor1)

    # Create and add a course using the Course class
    course1 = Course("Intro to Programming", 1001)
    sms.add_course(course1)

    # Enroll students in the course
    sms.enroll_student(course1, 56, student1)
    sms.enroll_student(course1, 98, student2)
    
    print(sms.students)
    print(sms.instructors)
    print(sms.courses)
    print(sms.enrollments)

    # Display course enrollment
    #print("Students in course:", sms.get_students_in_course(str(course1)))
    #print(f"Courses for {student1.name}:", sms.get_courses_for_student(str(student1)))

if __name__ == "__main__":
    main()
