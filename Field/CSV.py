import csv

with open('~/LanguageProject/dictionary.csv', 'r') as Dcsv:
    Dreader = csv.reader(Dcsv)
    for row in Dreader:
        print(row)
