#create a dictionary for a subset of your data
import csv

diction = {}

with open("pokemon.csv", encoding="utf-8", errors="replace") as fileIn:
    reader = csv.reader(fileIn)
    title = fileIn.readline()
    title = title.split(",")

    for line in reader:
        temp = []

        temp.append(line[5])  #hp
        temp.append(line[6])  #atk
        temp.append(line[7])  #def
        temp.append(line[8])  #sp. atk
        temp.append(line[9])  #sp. def
        temp.append(line[10]) #spd
        
        
        
        if line[3]== "Fairy":
            diction[line[1]]=temp
        elif line[2]== "Fairy":
            diction[line[1]]=temp
            
    intro = '＊*•̩̩͙✩•̩̩͙*˚‧͙⁺˚*･༓☾　FAIRY POKEMON　☽༓･*˚⁺‧˚*•̩̩͙✩•̩̩͙*˚͙\n\n'
    print('\n\n')
    print(intro.center(100))
    print(f'{title[1]:<40}{title[5]:<7}{title[6]:<10}{title[7]:<10}{title[8]:<10}{title[9]:<12}{title[10]:<10}\n')
    for key in diction:
        print(f'{key:<40}{diction[key][0]:<10}{diction[key][1]:<10}{diction[key][2]:<10}{diction[key][3]:<10}{diction[key][4]:<10}{diction[key][5]:<10}')
