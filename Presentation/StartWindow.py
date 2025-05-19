import sys
import os
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from os.path import basename
from PyQt5.QtCore import QPoint, Qt, QRect
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QPushButton, QMenu, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen
sys.path.insert(1, 'C:\\Users\\Hello\\python\\FinalProject_IVP501_6\\ORC_Snipping_Tool\\Presentation')
import SnippingToolWindow 

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SnippingTool')
        self.snippingTool = SnippingToolWindow.SnippingWidget()

        self.lastPoint = QPoint()


        # Create buttons
        button1 = QPushButton('New snipping', self)
        button2 = QPushButton('Exit', self)

        # Connect buttons to their respective functions
        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)

        # Create a vertical layout
        button1.move(0,0)
        button2.move(100,0)

        
        #self.setLayout(hbox)

        self.setGeometry(1500, 200, 400, 100)
        
        self.show()

    def button1_clicked(self):
        print('Snipping clicked')
        # Add your desired action for Button 1 here
        # For example:
        # self.label.setText("Button 1 clicked!")
        if self.snippingTool.background:
            self.close()
        self.snippingTool.start()
        self.close()

        
    def button2_clicked(self):
        print('Exit clicked')
        self.close()
        # Add your desired action for Button 3 here


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    sys.exit(app.exec_())