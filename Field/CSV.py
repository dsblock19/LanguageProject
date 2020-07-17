#Libraries
import pymysql

con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'dictionary')
cur = con.cursor()

results = []
sql = "SELECT * FROM words;"

with self.con:
    try:
        self.cur.execute(sql)
        results = self.cur.fetchall()
        self.con.commit()
        for i in range(len(results)):
            stof = open('/home/pi/Desktop/MyCode/LanguageProject/Output/Dictionary.csv', 'a')
            stof.write(results[i])
            stof.close()
    except Exception as e:
        self.con.rollback()
        print(e)
