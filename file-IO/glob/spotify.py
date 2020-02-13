import glob
import csv

def insertSongData(songs,namesong,day,streams):
    if (streams != ""):
        songs[namesong][day] = (f'{streams} streams')
        
def insertSong(songs, namesong):
    songs[namesong] = {}
    
def findDayName(name):
    index = name.find(".")
    day = name[index-10:index]
    day = day.replace("-"," ")
    return day

def findStreams(line):
    streams = int(line[3])
    return streams
    
songs = {}
files = glob.glob('regional*.csv')

#format:  SongName by Artist: {date: # streams, date: #streams, etc }

for name in files:
    dayname = findDayName(name)

    with open(name, encoding="utf-8",errors="replace") as file:
        file.readline()
        title=file.readline()
        
        reader = csv.reader(file)
        for line in reader:
            streams = findStreams(line)
            day = findDayName(name)
            
            namesong = (f'{line[1]} by {line[2]}')
            if (namesong not in songs):
                insertSong(songs,namesong)
            insertSongData(songs,namesong,day,streams)

for i in songs:
    print(f'{i:<30}\n{songs[i]}')
