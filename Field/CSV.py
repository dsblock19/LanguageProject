import csv
import pymysql

con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'Sto')
cur = con.cursor()

#csvFilePath = input('CSV Filepath: ')


with open('/home/pi/LanguageProject/FoundationalFamilies.csv', 'r') as Dcsv:
    Dreader = csv.reader(Dcsv)
    for row in Dreader:
        print(row[0] + ', ' + row[1] + ', ' + row[2] + ', ' + row[3])

        sql = "INSERT INTO GenerationII VALUES('" + str(row[0]) + "','" + str(row[1]) + "','" + str(row[2]) + "','" + str(row[3]) + ");"
        try:
            cur.execute(sql)
            con.commit()
            print(' Success')
        except Exception as e:
            con.rollback()
            print(' Error: ' + e)
