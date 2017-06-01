import clr

clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Windows.Forms import Application, Form, Button
from System.Drawing import Size, Point


class MyForm(Form):
    def __init__(self):
        self.Text = 'Button'
        self.CenterToScreen()
        self.Size = Size(250, 200)

        btn = Button()
        btn.Parent = self
        btn.Text = "Quit"
        btn.Location = Point(50, 50)
        btn.Click += self.OnClick
        btn.MouseEnter += self.OnEnter


        def OnClick(self, sender, args):
            self.Close()


        def OnEnter(self, sender, args):
            btn.Text = "button entered"


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)
