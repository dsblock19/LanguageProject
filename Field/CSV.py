import csv
import pymysql.cursors

con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'Sto')
cur = con.cursor()

with open('/home/pi/LanguageProject/words.csv', 'r') as Dcsv:
    Dreader = csv.reader(Dcsv)
    for row in Dreader:
        print(row[0] + ', ' + row[1] + ', ' + row[2])

        sql = "INSERT INTO FoundationalFamilies VALUES('" + str(row[0]) + "','" + str(row[1]) + "','" + str(row[2]) + "');"
        try:
            cur.execute(sql)
            con.commit()
            print(' Success')
        except Exception as e:
            con.rollback()
            print(' Error: ' + e)
