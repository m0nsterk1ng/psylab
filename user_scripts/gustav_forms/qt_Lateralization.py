# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:58:02 2014

@author: code-breaker
"""

import os, sys
from PyQt4 import QtGui, QtCore, Qt
import numpy as np
import psylab.audio

class Interface(QtGui.QWidget):
    
    form_w = 0
    form_h = 0

    respIcon_w = 0
    respIcon_h = 0

    respArea_x = 0
    respArea_y = 0
    respArea_w = 0
    respArea_h = 0

    response = 0
    click_x = 0
    click_y = 0

    feedback = False
    
    def __init__(self, bg_image=None, feedback=None):
        super(Interface, self).__init__()
        
        if bg_image:
            self.form_bgImage = bg_image
        else:
            self.form_bgImage = os.path.join("Images","SmileyFaces","smileyface_headphones.jpg")

        if feedback:
            self.feedback = True
            if os.path.isfile(feedback):
                self.respIcon_file = feedback
                self.icon_folder = False
            else:
                self.icon_folder = feedback
                self.icon_set = psylab.audio.signal_io.get_consecutive_files(self.icon_folder,
                                                                        file_ext='.png',
                                                                        random = True)
        self.initUI()
        
    def feedback_show(self):
        x = self.click_x - round(self.respIcon_w/2)+self.respArea_x
        x = np.maximum(x,0)
        x = np.minimum(x,self.form_w)
        y = (self.respArea_h/2) - round(self.respIcon_h/2)+self.respArea_y
        y = np.maximum(y,0)
        y = np.minimum(y,self.form_h)
        if self.icon_folder:
            self.iconImage.setVisible(False)
            respIconraw = QtGui.QPixmap(os.path.join(self.icon_folder,self.icon_set.get_next()))
#            if respIconraw.width() > 48 or respIconraw.height() > 48:
#                respIconraw = respIconraw.scaled(48,48, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.iconImage.setPixmap(respIconraw)
            self.iconImage.update()
        self.iconImage.setGeometry(x,y,self.respIcon_w, self.respIcon_h)
        self.iconImage.setVisible(True)
        
        
    def feedback_hide(self):
        self.iconImage.setVisible(False)

    def response_click(self , event):
        self.click_x = event.pos().x()
        self.click_y = event.pos().y()
        response = float(event.pos().x())/self.width()
        self.response = round(response * 21)-10
        if self.feedback:
            self.feedback_show()
        print("Response: %f" % (self.response))

    def initUI(self):               
        
        # Load Background Image
        self.setWindowIcon(QtGui.QIcon('shs_head16.png'))
        self.bgImageraw = QtGui.QPixmap(self.form_bgImage)
        self.form_w = self.bgImageraw.width()
        self.form_h = self.bgImageraw.height()
        if self.form_w > 500 or self.form_h > 500:
            self.bgImageraw = self.bgImageraw.scaled(500,500, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.form_w = self.bgImageraw.width()
            self.form_h = self.bgImageraw.height()
        self.bgimage = QtGui.QLabel(self)
        self.bgimage.setBackgroundRole(QtGui.QPalette.Base)
        self.bgimage.setSizePolicy(QtGui.QSizePolicy.Ignored,
                QtGui.QSizePolicy.Ignored)
        
        # Draw mid-saggital line
        self.bgimagep = QtGui.QPainter(self.bgImageraw)
        self.bgimagep.setPen(QtGui.QPen(QtGui.QColor(128, 128, 128), 6, QtCore.Qt.DotLine, QtCore.Qt.SquareCap, QtCore.Qt.BevelJoin));
        self.bgimagep.drawLine(int(self.form_w/2),0,int(self.form_w/2.),self.form_h)
        self.bgimage.setPixmap(self.bgImageraw)
        self.bgimagep.end()

        # Create response area
        self.respArea_x = 5
        self.respArea_y = int(self.form_h/4)
        self.respArea_w = self.form_w-10
        self.respArea_h = 35
        self.respArea = QtGui.QLabel(self)
        self.respArea.setGeometry(QtCore.QRect(self.respArea_x, self.respArea_y, self.respArea_w, self.respArea_h))
        self.respArea.setAutoFillBackground(True)
        self.respArea.setStyleSheet("border-style: outset; border-width: 3px; border-color: rgba(20,20,20,120); background-color: rgba(60,60,60,120); color: rgba(255,255,255,255);")
        self.respArea.mousePressEvent = self.response_click
        self.respArea.setAlignment(QtCore.Qt.AlignCenter)
        self.respArea.setAlignment(QtCore.Qt.AlignHCenter)

        if self.feedback:
            if self.icon_folder:
                respIconraw = QtGui.QPixmap(os.path.join(self.icon_folder,self.icon_set.get_next()))
            else:
                respIconraw = QtGui.QPixmap(self.respIcon_file)
            self.respIcon_w = respIconraw.width()
            self.respIcon_h = respIconraw.height()
            self.iconImage = QtGui.QLabel(self)
            self.iconImage.setBackgroundRole(QtGui.QPalette.Base)
            self.iconImage.setSizePolicy(QtGui.QSizePolicy.Ignored,
                    QtGui.QSizePolicy.Ignored)
            self.iconImage.setPixmap(respIconraw)
            self.iconImage.setVisible(False)

        #self.listenPrompt = QtGui.QLabel(self)
        #self.listenPrompt.setGeometry(QtCore.QRect(0, 0, self.form_w, self.form_h))
        #self.listenPrompt.setStyleSheet("qproperty-alignment: AlignCenter; background-color: rgba(100,20,20,255); color: rgba(255,255,255,255); font: bold 36px;")
        #self.listenPrompt.setText('Listen!')
        #self.listenPrompt.setVisible(False)

        self.setFixedSize(self.form_w, self.form_h)
        self.setWindowTitle('Gustav!')
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Interface('/home/code-breaker/Projects/psylab/user_scripts/gustav_forms/Images/SmileyFaces/smileyface_headphones.jpg',
                           '/home/code-breaker/Projects/psylab/user_scripts/gustav_forms/Images/Butterflies')
    #ex = Interface()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()