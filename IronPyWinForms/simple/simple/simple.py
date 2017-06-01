import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import Application, Form

class MyForm(Form):
    def __init__(self):
        self.Text = 'Simple Web Form'
        self.Width = 350
        self.Height = 300
        self.CenterToScreen()


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)
