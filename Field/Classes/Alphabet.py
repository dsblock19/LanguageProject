#Libraries
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

class Alpha():

    def __init__(self):
        #Setup
        self.con = pymysql.connect('localhost', 'dblo', '1819Kirk!', 'dictionary')
        self.cur = self.con.cursor()

        # screen
        self.inky_display = InkyWHAT("red")
        self.inky_display.set_border(self.inky_display.WHITE)
        #img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        self.img = Image.new("P", (400, 300))
        self.draw = ImageDraw.Draw(self.img)
        self.stofontpath = '/home/pi/LanguageProject/Field/Classes/Fonts/sto-ith/sto-ith.ttf'
        self.stofont = ImageFont.truetype(self.stofontpath, 10)
        self.x = 0
        self.y = 0

        self.root = [ 'd', 't', 'k', 'z', 'n', 's', 'm\n', 'g', 'p', 'v', 'j', 'b', 'h', 'r\n', 'aw', 'o', 'u', 'a', 'oo', 'e', 'i:i\n', 'i', 'c', 'sh', 'th', 'st', 'ch', 'x']

    def Alpha(self):

        root = self.root.upper()
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
        #' -->
        root = root.replace("(", "")
        #' -->
        root = root.replace(",", "")

        self.draw.text((self.x, self.y), root, self.inky_display.RED, self.stofont)
        #flipped = img.rotate(90)
        #inky_display.set_image(flipped)
        self.inky_display.set_image(self.img)
        self.inky_display.show()

        print('')
