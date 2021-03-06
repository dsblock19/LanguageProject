#Libraries
import pymysql
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

class Add2Dic():

    def __init__(self):
        #Setup
        self.con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'Sto')
        self.cur = self.con.cursor()

        # screen
        self.inky_display = InkyWHAT("black")
        self.inky_display.set_border(self.inky_display.WHITE)
        #img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        self.img = Image.new("P", (400, 300))
        self.draw = ImageDraw.Draw(self.img)
        self.stofontpath = '/home/pi/LanguageProject/Field/Classes/Fonts/sto-ith/sto-ith.ttf'
        self.stofont = ImageFont.truetype(self.stofontpath, 70)
        self.x = 0
        self.y = 100

    def AddWord(self):
        print('')
        word = input('Word: ')
        defin = input('Definition: ')
        part = input('Part of Speech: ')
        generation = input('Generation: ')
        if generation == 'I':
            sql = "INSERT INTO FoundationalFamilies VALUES('" + str(word) + "','" + str(defin) + "','" + str(part) + "');"
        elif generation == 'II':
            sql = "INSERT INTO GenerationII VALUES('" + str(word) + "','" + str(defin) + "','" + str(part) + "','II');"

        #with self.con:
        try:
            self.cur.execute(sql)
            self.con.commit()
            print(' Success')

            root = word
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
                self.img = Image.new("P", (400, 300))
                self.draw = ImageDraw.Draw(self.img)

                self.draw.text((self.x, self.y), root, self.inky_display.RED, self.stofont)
                #flipped = img.rotate(90)
                #inky_display.set_image(flipped)
                self.inky_display.set_border(self.inky_display.WHITE)
                self.inky_display.set_image(self.img)
                self.inky_display.show()

        except Exception as e:
            self.con.rollback()
            print(e)
        print('')
