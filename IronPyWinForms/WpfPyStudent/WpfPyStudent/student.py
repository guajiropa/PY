class Student:
#
#   This is the Student base class file for 'WpfPyStudent' manager.
#
#

    def __init__(self, first_name, last_name, student_id):
        self.students = []
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.students.append(self)



