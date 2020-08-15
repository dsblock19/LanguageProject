#Libraries
import random
import pymysql
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

#Setup
con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'Sto')
cur = con.cursor()

# screen
inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)
#img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
img = Image.new("P", (400, 300))
draw = ImageDraw.Draw(img)
stofontpath = '/home/pi/LanguageProject/Field/Fonts/sto-ith/sto-ith.ttf'
stofont = ImageFont.truetype(stofontpath, 70)
x = 0
y = 100

print('')
pos = input('Part of Speech: ')
generation = input('Generation: ')
if generation == 'I':
    sql = "SELECT ALL * FROM FoundationalFamilies WHERE Part of Speech LIKE '" + pos + "';"
elif generation == 'II':
    sql = "SELECT ALL * FROM `GenerationII` WHERE `Part of Speech` LIKE '" + pos + "';"
#with con:
try:
    cur.execute(sql)
    results = cur.fetchall()
    con.commit()
    for i in range(len(results)):
        print(results[i])
except Exception as e:
    con.rollback()
    print(e)
