#Libraries
import pymysql

con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'dictionary')
cur = con.cursor()

results = []
sql = "SELECT * FROM words;"

with con:
    try:
        cur.execute(sql)
        results = cur.fetchall()
        con.commit()
        for i in range(len(results)):
            stof = open('/home/pi/LanguageProject/Output/Dictionary.csv', 'a')
            res = str(results[i])
            res = res.replace("'" , '')
            res = res.replace(', ' , '/' )
            res = res.replace('(' , '' )
            res = res.replace(')' , '' )
            stof.write(res + '\n')
            stof.close()
    except Exception as e:
        con.rollback()
        print(e)
