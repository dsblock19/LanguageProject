import csv

with open('/home/pi/LanguageProject/words.csv', 'r') as Dcsv:
    Dreader = csv.reader(Dcsv)
    for row in Dreader:
        print(row[0] + ', ' + row[1] + ', ' + row[2])
