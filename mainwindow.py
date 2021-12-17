from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QPushButton, QLabel, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import discogs_client
import urllib.request
import re
import pafy
from urllib.request import urlretrieve
import random
from PIL import Image, ImageEnhance

d = discogs_client.Client('FindTune/1.0', user_token=<your user token goes here>)

trackname = list()

class SongRecommendWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("recompage.ui", self) #recomendations window time

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
        #saving_input(self)
        mytext = self.textbox.toPlainText()
        with open('input.txt', 'w') as f: #saving user input
            f.write(mytext)
            print("input accepted") #debug

        with open('input.txt', 'r') as f:
            slist = f.readlines()
        
        inp = []
        for i in slist:
            s = i.split('-', 1)
            inp.append(s)
        print(inp) #debug

        songlist = []
        artistlist = []
        genrelist1 = []
        genrelist2 = []
        for i in inp:
            song = i[0]
            a = i[1]
            inpresults = d.search(song, artist=a, type='release')
            artid = inpresults[0].id
            res2 = d.release(artid)
            print(res2.genres) #debug
            g1 = res2.genres[0]
            if len(res2.genres)>1: g2 = res2.genres[1] 
            else: g2="empty"
            if g2!="empty": print(song, a, g1, g2) 
            else: print(song,a,g1)

            songlist.append(song)
            artistlist.append(a)
            genrelist1.append(g1)
            genrelist2.append(g2)

        def youtubesearch(idn, namee):
            print(idn)
            release = d.release(idn)
            leng = len(release.tracklist)
            print(leng)
            i = random.randint(0,leng)
            print(i)
            stitle = release.tracklist[i].title
            artist = release.artists[0].name
            title = stitle+' by '+artist
            global trackname
            trackname.append(title)
            print(title)
            query = title.replace(" ", "+")
            print(query)
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
            video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            video_url = "https://www.youtube.com/watch?v=" + video_id[0]
            print(video_url)
            video = pafy.new(video_url, basic=True, gdata=False)
            thumb = video.bigthumb
            filename = namee+'.jpg'
            print(filename)
            urlretrieve(thumb, filename)
        
        for artist in artistlist:
            artsrch = d.search(artist=artist, type='release')
            artrecom1 = artsrch[0].id
            artrecom2 = artsrch[1].id
            print(artrecom1)
            print(artrecom2)
            youtubesearch(artrecom1, "rec1")
            youtubesearch(artrecom2, "rec2")

        for genre in genrelist1:
            gensrch = d.search(genre=genre, type='release')
            genrecom1 = gensrch[0].id
            genrecom2 = gensrch[1].id
            genrecom3 = gensrch[2].id
            genrecom4 = gensrch[3].id
            print(genrecom1)
            print(genrecom2)
            print(genrecom3)
            print(genrecom4)
            youtubesearch(genrecom1, "rec3")
            youtubesearch(genrecom2, "rec4")
            youtubesearch(genrecom3, "rec5")
            youtubesearch(genrecom4, "rec6")
        
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

#initialize the app
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
