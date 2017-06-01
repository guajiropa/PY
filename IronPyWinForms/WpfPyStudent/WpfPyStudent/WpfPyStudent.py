#
#   AUTHOR      :   Robert James Patterson
#   DATE        :   05/16/17
#   SYNOPSIS    :   A simple IronPython 2.7 / XAML test built with Visual Studio 2017 preview release.
#    

import wpf
from System.IO import *
from System.Windows import Application, Window


class Student:
#
#   This is the Student class file for 'WpfPyStudent' manager.
#   
    
    def write_student_file(self, new_student):
    #Method to write the student data to file

        sw = StreamWriter
        fs = FileStream
        
        student_data = [new_student.first_name, 
                         new_student.last_name,
                         new_student.student_id]       
         
        #Open the file for appending. 
        if not File.Exists("students.txt"):
            Try:
                fs = File.Create("students.txt")
                sw = File.AppendText("students.txt")
                sw.WriteLine(student_data)
            Except Exception as e:
                pass
        elif
            sw = File.AppendText("students.txt")
            sw.WriteLine(student_data)
            sw.Close()
            
        #Clear the form fields after the write
        MyWindow.txt_first_name.Text = ""
        MyWindow.txt_last_name.Text = ""
        MyWindow.txt_student_id = ""
        
    #Class initilizer
    def __init__(self, first_name='', last_name='', student_id=''):
        #Initialize 
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
    
#=====================================================================================================

class MyWindow(Window):

               
    def btn_cancel_Click(self, sender, e):
        Application.Shutdown()

    def btn_save_Click(self, sender, e):
        
        #Create a new Student object from the Student() class.
        new_student = Student()
        
        #Grab the values from the XAML form and populate the Student object.
        new_student.first_name = self.txt_first_name.Text
        new_student.last_name = self.txt_last_name.Text
        new_student.student_id = self.txt_student_id.Text
        new_student.write_student_file(new_student)    
        
    def btn_reset_Click(self, sender, e):
        self.txt_first_name.Text = ""
        self.txt_last_name.Text = ""
        self.txt_student_id = ""
     
    def load_error_msg(self, e):
        wpf.LoadComponent(self, 'error_reporter.xaml')
        self.lbl
    def __init__(self):
        wpf.LoadComponent(self, 'WpfPyStudent.xaml')

if __name__ == '__main__':
    Application().Run(MyWindow())
