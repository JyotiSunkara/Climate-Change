from os import listdir
from os.path import isfile, join


sample = open('cleaned-data.csv', 'a')

onlyfiles = [f for f in listdir("./ghcnd_all") if isfile(join("./ghcnd_all", f))]
print(len(onlyfiles))
count = 0
for file in onlyfiles:
    maximum = 10000
    minimum = 10000 
    print("opening", file, count)
    count += 1
    file1 = open("./ghcnd_all/" + file, 'r') 
    Lines = file1.readlines()
    for line in Lines: 
        row = line.strip()
        if row[17:21] == "TMAX":
            for x in range(21,262,8):
                val = (int(row[x:x+5]))/10
                if maximum == 10000 and val > -100:
                    maximum = val
                    date = row[11:15] +"/"+ row[15:17] +"/"+ str(int((x-21)/8)+1)
                    string = row[0:11] + "," + date + ","+ str( maximum ) +"," + "max"
                    print(string, file = sample)

                elif val > maximum and val > -100:
                    maximum = val
                    date = (row[11:15]) +"/"+ (row[15:17]) +"/"+ str(int((x-21)/8)+1)
                    string = row[0:11] + "," + date + ","+ str( maximum ) +"," + "max"
                    print(string, file = sample)
        
        if row[17:21] == "TMIN":
            for x in range(21,262,8):
                val = (int(row[x : x+5]))/10
                if minimum == 10000 and val > -100:
                    minimum = val
                    date = (row[11:15]) +"/"+ (row[15:17]) +"/"+ str(int((x-21)/8)+1)
                    string = row[0:11] + "," + date + "," + str( minimum ) + "," + "min"
                    print(string, file = sample)

                elif val < minimum and val > -100:
                    minimum = val
                    date = (row[11:15]) +"/"+ (row[15:17]) +"/"+ str(int((x-21)/8)+1)
                    string = row[0:11] + "," + date + "," + str( minimum ) + "," + "min"
                    print(string, file = sample)


sample.close()