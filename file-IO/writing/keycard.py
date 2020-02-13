import csv
import random

with open("keycard.csv","w",newline='',errors="replace") as fileOut:
    writer = csv.writer(fileOut)
    title=['ID','Name','Occupation','Salary']
    writer.writerow(title)

    with open("names.txt", encoding="utf-8", errors="replace") as namesIn:
        names=[]
        for name in namesIn:
            n = name.strip()
            names.append(n)
        
    with open("jobs.txt", encoding="utf-8", errors="replace") as jobsIn:
        jobs=[]
        for job in jobsIn:
            j = job.strip()
            jobs.append(j)
                
    for i in range(500):       
        ID=''
        for k in range(9):
            ID += str(random.randint(1,9))
        id_key=(f'{ID[0:3]}-{ID[3:5]}-{ID[5:]}')
        
        s = str(random.randint(25000,125000))
        salary = '$'+s[:-3]+','+s[-3:]
        
        data=[]
        data.append(id_key)        
        data.append(names[i])
        data.append(jobs[random.randint(0,len(jobs)-1)])
        data.append(salary)
        writer.writerow(data)

fileOut.close()
