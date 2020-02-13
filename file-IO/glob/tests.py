import csv
import glob

files = glob.glob("regional-global-daily-2019-09-16.csv")
for names in files:
    with open (names, encoding="utf-8", errors="replace") as fileIn:
        fileIn.readline()
        
##        reader=csv.DictReader(fileIn)
##        for line in reader:
##            if line["Position"] == "1":
##                print(line["Track Name"])
            
##        reader=csv.reader(fileIn)
##        for line in reader:
##            if line[0] == "1":
##                print(line[1])


