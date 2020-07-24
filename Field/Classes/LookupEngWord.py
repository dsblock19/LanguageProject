#Libraries
import pymysql
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

class LookUpEng():

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

    def WordDefEng(self):
        print('')
        word = input('Word: ')
        generation = input('Generation: ')
        if generation == 'I':
            sql = "SELECT ALL * FROM FoundationalFamilies WHERE definition LIKE '%" + word + "%';"
        elif generation == 'II':
            sql = "SELECT ALL * FROM GenerationII WHERE definition LIKE '%" + word + "%';"
        #with self.con:
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            self.con.commit()
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
