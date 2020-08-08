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
    sql = "SELECT ALL * FROM FoundationalFamilies WHERE part of speech LIKE '%" + pos + "%';"
elif generation == 'II':
    sql = "SELECT ALL * FROM GenerationII WHERE part of speech LIKE '%" + pos + "%';"
#with con:
try:
    cur.execute(sql)
    results = cur.fetchall()
    con.commit()
    for i in range(len(results)):
        print(results[i])
    root = results[0]
    root = root[0]
    root = root.upper()
    #Font Specific Change
    #ST --> F
    root = root.replace('ST', 'F')
    #OO --> L
    root = root.replace('OO', 'L')
    #SH --> Q
    root = root.replace('SH', 'Q')
    #AW --> W
    root = root.replace('AW', 'W')
    #I:I --> Y
    root = root.replace('I:I', 'Y')
    #CH --> @
    root = root.replace('CH', '@')
    #TH --> #
    root = root.replace('TH', '#')
    #' -->
    root = root.replace("'", "")

    print('')
    eink = input('Inky? ')
    eink = eink.upper()
    if eink == 'YES':
        img = Image.new("P", (400, 300))
        draw = ImageDraw.Draw(img)

        draw.text((x, y), root, inky_display.RED, stofont)
        #flipped = img.rotate(90)
        #inky_display.set_image(flipped)
        inky_display.set_border(inky_display.WHITE)
        inky_display.set_image(img)
        inky_display.show()
except Exception as e:
    con.rollback()
    print(e)
