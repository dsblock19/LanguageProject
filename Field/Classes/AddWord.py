#Libraries
import pymysql
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

class Add2Dic():

    def __init__(self):
        #Setup
        self.con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'dictionary')
        self.cur = self.con.cursor()

    def AddWord(self):
        print('')
        word = input('Word: ')
        defin = input('Definition: ')
        part = input('Part of Speech: ')
        sql = "INSERT INTO words VALUES('" + str(word) + "','" + str(defin) + "','" + str(part) + "');"
        with self.con:
            try:
                self.cur.execute(sql)
                self.con.commit()
                print(' Success')
            except Exception as e:
                self.con.rollback()
                print(e)
        print('')
