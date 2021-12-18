import discogs_client
import urllib.request
import re
import pafy
from urllib.request import urlretrieve
import random
from unidecode import unidecode

d = discogs_client.Client('FindTune/1.0', user_token='XwlgRFJZsoNbmZldzgGGQhTNQpQmMTuNDQJVDSdG')

tracknamee = list()

def tracklistop(tracknamee):
    return tracknamee

def youtubesearch(idn, namee):
    print(idn)
    release = d.release(idn)
    leng = len(release.tracklist)
    print(leng)
    i = random.randint(0,leng-1)
    print(i)

    stitle = release.tracklist[i].title
    artist = release.artists[0].name
    title = stitle+' by '+artist
    global tracknamee
    tracknamee.append(title)
    print(title)
    quer = title.replace(" ", "+")
    print(quer)
    query = unidecode(quer)
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
        
def saving_input(self):
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
        era = inpresults[0].year
        print(era)
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

    for artist in artistlist:
        artsrch = d.search(artist=artist, year=era, type='release')
        artrecom1 = artsrch[0].id
        artrecom2 = artsrch[1].id
        print(artrecom1)
        print(artrecom2)
        youtubesearch(artrecom1, "rec1")
        youtubesearch(artrecom2, "rec2")

    for genre in genrelist1:
        gensrch = d.search(genre=genre, year=era, type='release')
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
        tracklistop(tracknamee)
