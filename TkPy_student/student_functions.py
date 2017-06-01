 
#
# This is the main file for our Tkinter Student program    
# 

students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(str(student[0]).title())
        students_titlecase.append(str(student[1]).title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(first_name, last_name, student_id):
    student = {"first_name": first_name, 
               "last_name": last_name, 
               "student_id": student_id}
    students.append(student)
    

def save_file(student):
    with open("students.txt", "a") as f:
        f.write("{0}, {1} - {2}".format(new_student[1], 
                                        new_student[0],
                                        new_student[2])+ "\n")
        
def read_file():
    with open("students.txt", "r")as f:
        for student in f.readlines():
            add_student(student[0], 
                        student[1], 
                        student[2])

read_file()

print_students_titlecase()

more_students = True

while more_students is True:
    student_first_name = input("Enter student first name: ")
    student_last_name = input("Please eenter student last name: ")
    student_id = input("Enter student ID: ")
    new_student = [student_first_name, student_last_name, student_id]
    yn = input("Would you like to enter another student? [y/n]:")
    if yn == 'n' or 'N':
        print_students_titlecase()
        break
    continue

add_student(student_first_name, student_last_name, student_id)
save_file(new_student)

