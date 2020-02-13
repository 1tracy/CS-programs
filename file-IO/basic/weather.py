import csv
import itertools
# Create a Dictionary of Lists for stations with mean temperature higher than 0.

diction = {}

with open("weather.csv", encoding="utf-8", errors="replace") as fileIn:
    reader = csv.reader(fileIn)
    for line in itertools.islice(fileIn,32,None):
        line = line.split(",")
        if line[5].count(".")==1:
            mean = round(float(line[5]))
        elif line[5] == "":
            mean = -1
        else:
            mean = int(line[5])

        if mean>0:
            diction[line[0]]=mean
            
    print('Station Name'+' '*39 +'Temperature\n')
    for key in diction:
        print(f'{key:<50} {diction[key]:<3}Celsius')
