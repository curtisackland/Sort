from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPalette, QColor
app = QApplication([])

# Dark Theme
dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53,53,53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(dark_palette)


window = QWidget()
layout = QVBoxLayout()
layout2 = QHBoxLayout()
top = QPushButton('Top')
layout.addWidget(top)
layout2.addWidget(QPushButton('Test1'))
layout2.addWidget(QPushButton('Test2'))
layout.addLayout(layout2)
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()

def clicktest():
    layout.addWidget(QLabel('Bottom text'))
    print("Hello")

top.clicked.connect(clicktest)


app.exec()
print("test")