import wpf

from System.Windows import Window

class error_reporter(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'error_reporter.xaml')
