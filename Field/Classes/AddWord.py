#Libraries
import pymysql

class Add2Dic():

    def __init__(self):
        #Setup
        self.con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'Dictionary')
        self.cur = self.con.cursor()

    def AddWord(self):
        word = input('Word: ')
        defin = input('Definition: ')
        sql = "INSERT INTO words VALUES ('" + word + "','" + defin + "' ) ;'"
        try:
            self.cur.execute(sql)
            self.con.commit()
        except Exception:
            print('Failed')
