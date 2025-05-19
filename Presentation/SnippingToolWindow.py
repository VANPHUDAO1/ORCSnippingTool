import sys
import os

import tkinter as tk
import numpy as np
import cv2
from PIL import ImageGrab
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

sys.path.insert(1, 'C:\\Users\\Hello\\python\\FinalProject_IVP501_6\\ORC_Snipping_Tool\\Presentation')

import ORCProcessingWindow 

class SnippingWidget(QtWidgets.QWidget):
    background = True
    def __init__(self, parent = None):
        super(SnippingWidget, self).__init__()
        self.parent = parent
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

        
        

    def start(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        SnippingWidget.background = False
        self.setWindowOpacity(0.3)
        #QtWidgets.QApplication.setOverrideCursor(
        #    QtGui.QCursor(QtCore.Qt.CrossCursor)
        #)

        SnippingWidget.background = False
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        #img.save('capture.png')
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

        #cv2.imshow('Captured Image', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        self.w = ORCProcessingWindow.OrcSnippingWindow(img)
        self.w.show()
        
