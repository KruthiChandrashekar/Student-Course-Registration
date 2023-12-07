import mysql.connector

# Establish connection to MySQL
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Kruthi@2104",
    database="StudentManagement"
)

cursor = mydb.cursor()

def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS courses (course_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS student_course (student_id INT, course_id INT, FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id))")
    mydb.commit()

def enroll_student(name):
    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    mydb.commit()
    print(f"Student {name} enrolled successfully!")

def introduce_course(name, time):
    cursor.execute("INSERT INTO courses (name, time) VALUES (%s, %s)", (name, time))
    mydb.commit()
    print(f"Course {name} introduced successfully!")

def enroll_student_in_course(student_id, course_id):
    cursor.execute("INSERT INTO student_course (student_id, course_id) VALUES (%s, %s)", (student_id, course_id))
    mydb.commit()
    print(f"Student {student_id} enrolled in Course {course_id} successfully!")

def get_students_in_course(course_id):
    cursor.execute("SELECT students.name FROM students INNER JOIN student_course ON students.student_id = student_course.student_id WHERE student_course.course_id = %s", (course_id,))
    students = cursor.fetchall()
    if students:
        print(f"Students enrolled in Course {course_id}:")
        for student in students:
            print(student[0])
    else:
        print(f"No students enrolled in Course {course_id}.")

def get_courses_for_student(student_id, day):
    cursor.execute("SELECT courses.name, courses.time FROM courses INNER JOIN student_course ON courses.course_id = student_course.course_id WHERE student_course.student_id = %s", (student_id,))
    courses = cursor.fetchall()
    if courses:
        print(f"Courses for Student {student_id} on {day}:")
        for course in courses:
            print(f"Course: {course[0]}, Time: {course[1]}")
    else:
        print(f"No courses found for Student {student_id}.")

def main():
    create_tables()
    while True:
        print("\nWhat would you like to do?")
        print("1. Enroll a new student")
        print("2. Introduce a new course")
        print("3. Enroll a student in a course")
        print("4. Get students in a course")
        print("5. Get courses for a student on a day")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the student's name: ")
            enroll_student(name)
        elif choice == "2":
            name = input("Enter the course name: ")
            time = input("Enter the course time: ")
            introduce_course(name, time)
        elif choice == "3":
            student_id = input("Enter the student's ID: ")
            course_id = input("Enter the course ID: ")
            enroll_student_in_course(student_id, course_id)
        elif choice == "4":
            course_id = input("Enter the course ID: ")
            get_students_in_course(course_id)
        elif choice == "5":
            student_id = input("Enter the student's ID: ")
            day = input("Enter the day: ")
            get_courses_for_student(student_id, day)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
