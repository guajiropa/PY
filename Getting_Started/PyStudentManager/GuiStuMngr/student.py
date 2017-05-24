"""
#   Author      :   Robert James Patterson
#   Created     :   5/22/2017
#   Modified    :   5/22/2017
#   Project     :   student_class.py
#   Synopsis    :   This is the student object
#
"""


class Student:
    # This is a 'static' value of the 'Student()' class
    school_name = "Springfield Vocational Tech"

    def __init__(self):
        self.students = []
        self.first_name
        self.last_name
        self.student_id
        self.students.append(self)

    def get_name_capitalize(self):
        return self.first_name.capitalize(), self.last_name.capitalize()

