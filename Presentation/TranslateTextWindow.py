import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QAction, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class NewWindow(QWidget):
    def __init__(self, new_string):
        super().__init__()

        self.setWindowTitle("Text extract")

        # Create a label to display the new string
        #self.label = QLabel(new_string, self)
        #self.label.setFont(QFont('Arial', 16))
        #self.label.setWordWrap(True)
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)  # Make it display-only
        text_edit.setPlainText(new_string)
        
        # Set the font and font size
        font = QFont("Arial", 16)  # You can change the font family and size
        text_edit.setFont(font)
        #print(new_string)
        # Create a layout to arrange the label
        layout = QVBoxLayout()
        layout.addWidget(text_edit)

        self.setGeometry(1300, 150, 600, 300 )

        self.setLayout(layout)

        self.show()
        
