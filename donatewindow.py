from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel



class DonateWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("                 Thank you for using SkyMacro.\n If you like it consider Donating via Paypal to:\n                     felipeqx090@gmail.com")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle('Thank You!')
        self.resize(260, 122)

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Instructions:\n macro_file.txt must be in the same folder of SkyMacro.\n\n For now you can't bind combined hotkeys ex:(ctrl+f).\n\n Events must be in this format example:\n\n q down(q key is being pressed)\n 0.030(30 ms delay)\n"
                            " q up(q key is being released)\n\n Delay is based in seconds, 1.000 equals one second delay.\n Complete list of avaiable hotkeys:")
        self.urllabel = QLabel()
        self.urllabel.setText('''<a href='https://pyautogui.readthedocs.io/en/latest/keyboard.html'>pyautogui Documentation</a>''')
        self.urllabel.setOpenExternalLinks(True)
        layout.addWidget(self.label)
        layout.addWidget(self.urllabel)
        self.setLayout(layout)
        self.setWindowTitle('Help')
        self.resize(260, 122)
