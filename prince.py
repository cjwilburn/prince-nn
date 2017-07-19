# import libraries
import urllib2
from urllib import FancyURLopener
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from random import choice

# specify the url
quote_page = ['http://www.songlyrics.com/prince/18-over-lyrics',
              'http://www.songlyrics.com/prince/adore-lyrics',
              'http://www.songlyrics.com/prince/hot-with-u-lyrics/',
              'http://www.songlyrics.com/prince/get-some-solo-lyrics/',
              'http://www.songlyrics.com/prince/little-red-corvette-dance-mix-lyrics/',
              'http://www.songlyrics.com/prince/raspberry-beret-lyrics/',
              'http://www.songlyrics.com/prince/controversy-lyrics/',
              'http://www.songlyrics.com/prince/get-off-lyrics/',
              'http://www.songlyrics.com/prince/i-wish-u-heaven-part-12-3-lyrics/',
              'http://www.songlyrics.com/prince/all-the-critics-love-u-in-new-york-lyrics/',
              'http://www.songlyrics.com/prince/pop-life-lyrics/',
              'http://www.songlyrics.com/prince/200-balloons-lyrics/',
              'http://www.songlyrics.com/prince/i-rock-therefore-i-am-lyrics/',
              'http://www.songlyrics.com/prince/i-will-lyrics/',
              'http://www.songlyrics.com/prince/head-lyrics/',
              'http://www.songlyrics.com/prince/sister-lyrics/',
              'http://www.songlyrics.com/prince/she-s-just-a-baby-lyrics',
              'http://www.songlyrics.com/prince/sometimes-it-snows-in-april-lyrics',
              'http://www.songlyrics.com/prince/i-would-die-4-u-lyrics',
              'http://www.songlyrics.com/prince/she-loves-me-4-me-lyrics',
              'http://www.songlyrics.com/prince/just-as-long-as-we-re-together-lyrics',
              'http://www.songlyrics.com/prince/hot-thing-lyrics',
              'http://www.songlyrics.com/prince/i-feel-for-you-lyrics'
              'http://www.songlyrics.com/prince/diamonds-and-pearls-lyrics',
              'http://www.songlyrics.com/prince/wherever-u-go-whatever-u-do-lyrics',
              'http://www.songlyrics.com/prince/the-arms-of-orion-lyrics',
              'http://www.songlyrics.com/prince/drive-me-wild-lyrics/',
              'http://www.songlyrics.com/prince/freaks-on-this-side-lyrics/',
              'http://www.songlyrics.com/prince/purple-rain-lyrics/',
              'http://www.songlyrics.com/prince/the-most-beautiful-girl-in-the-world-lyrics/',
              'http://www.songlyrics.com/prince/irresistible-bitch-lyrics/']

# for loop
data = []
for pg in quote_page:
    # query the website and return the html to the variable 'page'
    # user agent
    req = urllib2.Request(pg, headers={'User-Agent': "Magic Browser"})
    page = urllib2.urlopen(req)
    # page = urllib2.urlopen(pg)

# parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
    song_box = soup.find('p', attrs={'class': 'songLyricsV14'})
    song = song_box.text.strip()

# save the data in tuple
    data.append((song))

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    # The for loop
    for song in data:
        writer.writerow([song])
