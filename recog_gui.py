# -*- coding: utf-8 -*-
from win32api import GetSystemMetrics
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.QtCore import QDir, Qt, QUrl,QThread,QRect
#from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
#from PyQt5.QtMultimediaWidgets import QVideoWidget
#from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTableWidget,QVBoxLayout,
#    QTableWidgetItem, QLabel, QHBoxLayout,QGridLayout)
from collections import deque
import cv2
import face_recognition
import numpy as np
import pickle
import face_lib as fl
import face_recognition


class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Face Recognition- safevision.ai'
        

        self.left = 0
        self.top = 0
        self.width = GetSystemMetrics(0) #640
        self.height = GetSystemMetrics(1) #480
        self.height = self.height - 50
        self.video = cv2.VideoCapture(0)
        self.all_encodings = fl.all_encoding()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 
        #self.resize(1200, 650) #1800,1200 width & height

        w = self.width
        print(w)
        w_frame = (w/100)*80
        h = self.height
        print(h)
        h_frame = (h/100)*100
        
        w_sub_frame = (w/100)*20
        h_sub_frame = (h/100)*20
        
        w_button = (h/100)*91

        
        layout = QWidget(self)
        label = QLabel(self)
        labell = QLabel(self)
        label_1 = QLabel(self)
        label_2 = QLabel(self)
        label_3 = QLabel(self)
        label_4 = QLabel(self)
        label_5 = QLabel(self)
        button = QLabel(self)

        label_img = QLabel(self)
        pixmap = QPixmap('logo.png')
        label_img.setPixmap(pixmap)
        label_img.setScaledContents(True)
        label_img.setGeometry(QtCore.QRect(0, 0, 140, 50))

        label_img1 = QLabel(self)
        pixmap1 = QPixmap('byteforce_logo.jpeg')
        label_img1.setPixmap(pixmap1)
        label_img1.setScaledContents(True)
        label_img1.setGeometry(QtCore.QRect(1500, 10, 140, 50))
#        
        stack = deque(["0","1","2","3","4"])
        stack.append("new")
        stack.popleft()
        i=1
       
        while True:
            rc, image = self.video.read()
            resultImage, Cropped = fl.recog_face(image,self.all_encodings)
            for loc in Cropped:
                top,right,bottom,left = loc
                crop_img=image[top:bottom,left:right]
                ii = "Cropped"+str(i)+".jpg"
                cv2.imwrite(ii, crop_img)
            stack.append(ii)
            stack.popleft()
            
           

           
            rgbImage = cv2.cvtColor(resultImage, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                             QtGui.QImage.Format_RGB888)
            convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
            pixmap = QPixmap(convertToQtFormat)
            #resizeImage = pixmap.scaled(900, 600) #changing 640,480 , QtCore.Qt.KeepAspectRatio
            resizeImage = pixmap.scaled(w_frame, h_frame)
            QApplication.processEvents()
            label.setPixmap(resizeImage)
            self.show()

            #label_1.setGeometry(QtCore.QRect(920, 0, 250, 160)) #Here x,y,width,height
            label_1.setGeometry(QtCore.QRect(5+w_frame, 0, w_sub_frame, h_sub_frame))
            img1 = stack[0]
            label_1.setPixmap(QtGui.QPixmap(img1))
            label_1.setScaledContents(True)
            

            #label_2.setGeometry(QtCore.QRect(920, 165, 250, 160))
            label_2.setGeometry(QtCore.QRect(5+w_frame, 1*h_sub_frame, w_sub_frame, h_sub_frame))
            img2 = stack[1]
            label_2.setPixmap(QtGui.QPixmap(img2))
            label_2.setScaledContents(True)
            
            #label_3.setGeometry(QtCore.QRect(920, 330, 250, 160))
            label_3.setGeometry(QtCore.QRect(5+w_frame, 2*h_sub_frame, w_sub_frame, h_sub_frame))
            img3 = stack[2]
            label_3.setPixmap(QtGui.QPixmap(img3))
            label_3.setScaledContents(True)
            
            #label_4.setGeometry(QtCore.QRect(920, 495, 250, 160))
            label_4.setGeometry(QtCore.QRect(5+w_frame, 3*h_sub_frame, w_sub_frame, h_sub_frame))
            img4 = stack[3]
            label_4.setPixmap(QtGui.QPixmap(img4))
            label_4.setScaledContents(True)

            #label_5.setGeometry(QtCore.QRect(920, 660, 250, 160))
            label_5.setGeometry(QtCore.QRect(5+w_frame, 4*h_sub_frame, w_sub_frame, h_sub_frame))
            img5 = stack[4]
            label_5.setPixmap(QtGui.QPixmap(img5))
            label_5.setScaledContents(True)
            # Write the frame into the file 'output.avi'
            #out.write(resultImage)


            if cv2.waitKey(33) == 27:
                break
        
        cv2.destroyAllWindows()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
