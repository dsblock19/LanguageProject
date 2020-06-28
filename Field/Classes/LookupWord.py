#Libraries
import pymysql

class LookUp():

    def __init__(self):
        #Setup
        self.con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'Dictionary')
        self.cur = self.con.cursor()

    def WordDef(self):
        word = input('Word: ')
        sql = "SELECT ALL * FROM words WHERE sto = '" + word + "';"
        with self.con:
            try:
                self.cur.execute(sql)
                results = self.cur.fetchone()
                self.con.commit()
                print(' ' + str(results[1]))
            except Exception:
                self.con.rollback()
                print(' Failed')
