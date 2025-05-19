import sys
import os
import cv2
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from os.path import basename
from PyQt5.QtCore import QPoint, Qt, QRect
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QPushButton, QMenu, QFileDialog, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen, QCursor
from googletrans import Translator
sys.path.insert(1, 'C:\\Users\\Hello\\python\\FinalProject_IVP501_6\\ORC_Snipping_Tool\\Presentation')
sys.path.insert(1, 'C:\\Users\\Hello\\python\\FinalProject_IVP501_6\\ORC_Snipping_Tool\\Testing')
sys.path.insert(1, 'C:\\Users\\Hello\\python\\FinalProject_IVP501_6\\ORC_Snipping_Tool\\Business')

import Service
#from docx import Document
import TextWindow
import TestingBeforeImageProcessing
import SnippingToolWindow
import TranslateTextWindow
class OrcSnippingWindow(QWidget):
    def __init__(self, image = None):
        super().__init__()

        self.setWindowTitle('Orc Processing')
        self.snippingTool = SnippingToolWindow.SnippingWidget()
        self.lastPoint = QPoint()
        self.total_snips = 0
        self.image = image.copy()
        #print(image)

        # creating label
        self.label = QLabel(self)
        self.label.move(50,50)

        if image is not None:
            new_image = self.convert_numpy_img_to_qpixmap(image.copy())
        else:
            new_image = QPixmap("ImageFoders/snip1.png")

        
        # adding image to label
        self.label.setPixmap(new_image)
 
        # Optional, resize label to image size
        self.label.resize(new_image.width(),
                          new_image.height() + self.label.height())
        
        # Create buttons
        button0 = QPushButton('New snip', self)
        button1 = QPushButton('Text detection', self)
        button2 = QPushButton('Spell check', self)
        button3 = QPushButton('Translate', self)       
        button4 = QPushButton('Save to text file', self)
        button5 = QPushButton('Extract text', self)
        button6 = QPushButton('Edit image', self)
        button7 = QPushButton('Exit', self)

        # Connect buttons to their respective functions
        button0.clicked.connect(self.button0_clicked)

        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)
        button3.clicked.connect(self.button3_clicked)
        button4.clicked.connect(self.button4_clicked)
        button5.clicked.connect(self.button5_clicked)
        button6.clicked.connect(self.button6_clicked)
        button7.clicked.connect(self.button7_clicked)

        # Create a vertical layout
        button0.move(0,0)
        button1.move(100,0)
        button2.move(200,0)
        button3.move(300,0)
        button4.move(400,0)
        button5.move(500,0)
        button6.move(600,0)
        button7.move(700,0)
        
        #self.setLayout(hbox)

        self.setGeometry(300, 300, new_image.width() + 200, new_image.height() + 100)

        
        self.show()
    def button0_clicked(self):
        print('New Snipping clicked')
        # Add your desired action for Button 1 here
        # For example:
        # self.label.setText("Button 1 clicked!")
        self.snip = SnippingToolWindow.SnippingWidget()
        if self.snip.background:
            self.close()
        self.snip.start()
        self.close()



    def button1_clicked(self):
        print('Text detection clicked')
        # Add your desired action for Button 1 here
        # For example:
        # self.label.setText("Button 1 clicked!")
        image = Service.box_all_word_image_service(self.image)
        # Display the image
        cv2.imshow('Image', image)
        # Wait for a key press to close the window
        cv2.waitKey(0)
        # Close all windows
        cv2.destroyAllWindows()

    def button2_clicked(self):
        print('Spell check clicked')
        # Add your desired action for Button 2 here
        image = Service.box_wrong_word_image_service(self.image)
        # Display the image
        cv2.imshow('Image', image)
        # Wait for a key press to close the window
        cv2.waitKey(0)
        # Close all windows
        cv2.destroyAllWindows()

    def button3_clicked(self):
        print('Translate to vietnamese')
        # Add your desired action for Button 2 here   
        dest_lang='vi'  
        translateText = Service.extract_text_service(self.image)
        
        #print(continuous)
        translator = Translator()
        translation = translator.translate(translateText, dest=dest_lang)

        self.new_window = TranslateTextWindow.NewWindow(translation.text)
        self.new_window.show()

    
        
    def button4_clicked(self):
        print('Save to text file clicked')
        # Add your desired action for Button 2 here
        self.title = 'snipping'
        content = Service.extract_text_service(self.image)
        #print(content)
        file_path, name = QFileDialog.getSaveFileName(self, "Save file", self.title, "DOCX Document file (*.docx)")
        if file_path:
            with open(file_path, "a") as f:
                f.write(content)
            #self.change_and_set_title(basename(file_path))
            print(self.title, 'Saved')

    def button5_clicked(self):
        print('Extract text clicked')
        # Add your desired action for Button 2 here     
        self.new_window = TextWindow.NewWindow(Service.extract_text_service(self.image))
        self.new_window.show()

    def button6_clicked(self):
        print('Edit image clicked')

        # Example: Draw a rectangle and some text on the image using OpenCV
        edited_image = self.image.copy()
        cv2.rectangle(edited_image, (50, 50), (300, 100), (255, 255, 255), -1)
        cv2.putText(edited_image, "Edited by Python", (60, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)

        self.image = edited_image  # Update the internal image

        # Convert to QPixmap and update the label
        new_pixmap = self.convert_numpy_img_to_qpixmap(edited_image)
        self.label.setPixmap(new_pixmap)
        #self.label.resize(new_pixmap.width(), new_pixmap.height() + self.label.height())


    def button7_clicked(self):
        print('Exit clicked')
        self.close()
        # Add your desired action for Button 3 here
    

    def closeEvent(self, event):
        event.accept()

    @staticmethod
    def convert_numpy_img_to_qpixmap(np_img):
        height, width, channel = np_img.shape
        bytesPerLine = 3 * width
        return QPixmap(QImage(np_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped())
