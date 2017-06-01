import clr
import sys

clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Windows.Forms import Application, Form
from System.Windows.Forms import Button, ToolTip
from System.Diagnostics import Icon
from System.Drawing import Point, Size

class MyForm(Form):
    
    def __init__(self):
        # Create child controls and initialize form
        self.Text = 'Simple WinForms Example'
        self.Width = 350
        self.Height = 300
        
        try:
            self.Icon = Icon("images\web.ico")
        except Exception, e:
            print(e.msg)
            sys.exit(1)

        self.CenterToScreen()
        
 
       
Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)
