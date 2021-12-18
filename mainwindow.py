from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QPushButton, QLabel, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image, ImageEnhance
import logic.inputanalysis

class SongRecommendWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("recompage.ui", self) #recomendations window time
        
        trackname = logic.inputanalysis.tracknamee

        self.img1 = self.findChild(QLabel, "img1")
        self.txt1 = self.findChild(QLabel, "text_1")
        self.img2 = self.findChild(QLabel, "img1_2")
        self.txt2 = self.findChild(QLabel, "text_2")
        self.img3 = self.findChild(QLabel, "img1_3")
        self.txt3 = self.findChild(QLabel, "text_3")
        self.img4 = self.findChild(QLabel, "img1_4")
        self.txt4 = self.findChild(QLabel, "text_4")
        self.img5 = self.findChild(QLabel, "img1_5")
        self.txt5 = self.findChild(QLabel, "text_5")
        self.img6 = self.findChild(QLabel, "img1_6")
        self.txt6 = self.findChild(QLabel, "text_6")

        im = Image.open('rec1.jpg')
        enhancer = ImageEnhance.Brightness(im)
        im_output = enhancer.enhance(0.5)
        im_output.save('rec1.jpg')
        
        im2 = Image.open('rec2.jpg')
        enhancer = ImageEnhance.Brightness(im2)
        im2_output = enhancer.enhance(0.5)
        im2_output.save('rec2.jpg')
        
        im3 = Image.open('rec3.jpg')
        enhancer = ImageEnhance.Brightness(im3)
        im3_output = enhancer.enhance(0.5)
        im3_output.save('rec3.jpg')

        im4 = Image.open('rec4.jpg')
        enhancer = ImageEnhance.Brightness(im4)
        im4_output = enhancer.enhance(0.5)
        im4_output.save('rec4.jpg')

        im5 = Image.open('rec5.jpg')
        enhancer = ImageEnhance.Brightness(im5)
        im5_output = enhancer.enhance(0.5)
        im5_output.save('rec5.jpg')

        im6 = Image.open('rec6.jpg')
        enhancer = ImageEnhance.Brightness(im6)
        im6_output = enhancer.enhance(0.5)
        im6_output.save('rec6.jpg')
        
        pixmap = QPixmap('rec1.jpg')
        self.img1.setPixmap(pixmap)
        self.img1.setScaledContents(True)
        self.txt1.setText(trackname[0])

        pixmap = QPixmap('rec2.jpg')
        self.img2.setPixmap(pixmap)
        self.img2.setScaledContents(True)
        self.txt2.setText(trackname[1])

        pixmap = QPixmap('rec3.jpg')
        self.img3.setPixmap(pixmap)
        self.img3.setScaledContents(True)
        self.txt3.setText(trackname[2])

        pixmap = QPixmap('rec4.jpg')
        self.img4.setPixmap(pixmap)
        self.img4.setScaledContents(True)
        self.txt4.setText(trackname[3])

        pixmap = QPixmap('rec5.jpg')
        self.img5.setPixmap(pixmap)
        self.img5.setScaledContents(True)
        self.txt5.setText(trackname[4])

        pixmap = QPixmap('rec6.jpg')
        self.img6.setPixmap(pixmap)
        self.img6.setScaledContents(True)
        self.txt6.setText(trackname[5])
        self.show()


class SongInputWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("inputwindow.ui", self) #second window time
        
        self.textbox = self.findChild(QPlainTextEdit, "textbox")
        self.submitbutton = self.findChild(QPushButton, "submit")
        self.taxt = self.findChild(QLabel, "label")
        self.submitbutton.clicked.connect(self.clicker2)
        self.show()
        
    def clicker2(self, clicked):
        logic.inputanalysis.saving_input(self)
        SongInputWindow.hide(self) #moving to 3rd window
        self.w = SongRecommendWindow()
        self.w.show()
        

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        #loading the UI file
        uic.loadUi("findtuneui.ui", self)

        #defining the widgets
        self.gsbutton = self.findChild(QPushButton, "Getstart_button")

        #actions
        self.gsbutton.clicked.connect(self.clicker)

        #showing the app
        self.show()
    
    def clicker(self, checked): 
        MainWindow.hide(self)
        self.w = SongInputWindow()
        self.w.show()

def mainApp():
    app = QApplication(sys.argv) #initialize the app
    w = MainWindow()
    w.setWindowTitle("FindTune")
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    mainApp()
