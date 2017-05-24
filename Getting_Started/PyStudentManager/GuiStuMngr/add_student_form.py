"""
#   Author      :   Robert James Patterson
#   Created     :   5/22/2017
#   Modified    :   5/23/2017
#   Project     :   add_student_form.py
#   Synopsis    :   This is the file to build the gui to accept a new student and add 
#                   them to the database file. We are using SQLite3 for the database
#                   and PyQt for the gui. 
#
"""
# Import supporting modules for the AddStudentForm() class.
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sqlite3


class AddStudentForm(QDialog):
    """ This class builds the data entry form that allows the end 
        user to add another student to the student database file.
    """

    def __init__(self):
        QDialog.__init__(self)
        """ This is the initializer, note that we also
            initialize an instance of the parent class.
        """

        # Setup the layouts for this form
        layout = QGridLayout()

        # Grab the components need for this form
        # and set them with their default values.
        self.first_name_lbl = QLabel("First name:")
        self.first_name_txt = QLineEdit()
        self.last_name_lbl = QLabel("Last name:")
        self.last_name_txt = QLineEdit()
        self.student_id_lbl = QLabel("Student ID#:")
        self.student_id_txt = QLineEdit()
        self.write_button = QPushButton("Save")
        self.clear_button = QPushButton("Clear")
        self.close_button = QPushButton("Close")
        self.first_name_txt.setPlaceholderText("Student's first name")
        self.last_name_txt.setPlaceholderText("Student's last name")
        self.student_id_txt.setPlaceholderText("Student ID number")

        # Add the widgets to the layout and state their
        # positions on the grid.
        layout.addWidget(self.first_name_lbl, 1, 0)
        layout.addWidget(self.first_name_txt, 1, 1)
        layout.addWidget(self.last_name_lbl, 2, 0)
        layout.addWidget(self.last_name_txt, 2, 1)
        layout.addWidget(self.student_id_lbl, 3, 0)
        layout.addWidget(self.student_id_txt, 3, 1)
        layout.addWidget(self.write_button, 4, 0)
        layout.addWidget(self.clear_button, 4, 1)
        layout.addWidget(self.close_button, 4, 2)

        # Pull it all together and setup this form
        self.setLayout(layout)
        self.setWindowTitle("Add a student")
        self.setWindowIcon(QIcon('PyLogo.png'))
        self.setStyleSheet("background-color: rgb(185, 200, 200);\n")
        self.setFocus()

        # Event handler for the close_button clicked event.
        self.close_button.clicked.connect(sys.exit)

        # Event handler for the clear_button clicked event.
        self.clear_button.clicked.connect(self.reset_form)

        # Event handler for the write_button clicked event.
        self.write_button.clicked.connect(self.write_to_file)

    def reset_form(self):
        """ This method resets the text boxes to blanks.
        """
        self.first_name_txt.setText("")
        self.last_name_txt.setText("")
        self.student_id_txt.setText("")

    def write_to_file(self):
        """ This is the method that writes the student
            student data to the database file.
        """
        first_name = self.first_name_txt.text()
        last_name = self.last_name_txt.text()
        student_id = self.student_id_txt.text()

        try:
            # Connect to the database file.
            db = sqlite3.connect('studata')
            # Create the cursor.
            cursor = db.cursor()
            # Load it with the SQL statement & execute.
            cursor.execute(''' INSERT INTO students(first_name, last_name, student_id)
                            VALUES(?,?,?) ''', (first_name, last_name, student_id))
            # Commit the changes to the database.
            db.commit()
            # Close the database file.
            db.close()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("An error has occurred : ")
            msg.setInformativeText(str(e))
            msg.setWindowTitle("ERROR")
            msg.show()

        # Reset the form.
        self.reset_form()


def main():
    app = QApplication(sys.argv)
    frm = AddStudentForm()
    frm.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
