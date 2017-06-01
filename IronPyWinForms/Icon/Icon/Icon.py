import clr
import sys

clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import Icon
from System.Windows.Forms import Application, Form

class MyForm(Form):
    def __init__(self):
        self.Text = 'Icon'
        self.Width = 350
        self.Height = 300

        try:
            self.Icon = Icon("web.ico")
        except Exception, e:
            print e.msg
            sys.exit(1)

        self.CenterToScreen()


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)
