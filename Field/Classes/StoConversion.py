#LIBRARIES
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw


class StoConversion():

    def __init__(self):
        #SETUP
        # screen
        self.inky_display = InkyWHAT("red")
        self.inky_display.set_border(self.inky_display.WHITE)
        #img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        self.img = Image.new("P", (400, 300))
        self.draw = ImageDraw.Draw(self.img)
        self.stofontpath = '/home/pi/LanguageProject/Field/Classes/Fonts/sto-ith/sto-ith.ttf'
        self.stofont = ImageFont.truetype(self.stofontpath, 70)
        self.x = 0
        self.y = 100

    #Build New Family
    def InSto(self):
        #SETUP
        # screen
        inky_display = InkyWHAT("red")
        inky_display.set_border(inky_display.WHITE)
        #img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        img = Image.new("P", (400, 300))
        draw = ImageDraw.Draw(img)
        stofontpath = '/home/pi/LanguageProject/Field/Classes/Fonts/sto-ith/sto-ith.ttf'
        stofont = ImageFont.truetype(stofontpath, 70)

        root = input('\nWord: ')
        print('')
        #Make Upper Case
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

        self.img = Image.new("P", (400, 300))
        self.draw = ImageDraw.Draw(self.img)
        self.draw.text((self.x, self.y), root, self.inky_display.RED, self.stofont)
        #flipped = img.rotate(90)
        #inky_display.set_image(flipped)
        self.inky_display.set_border(self.inky_display.WHITE)
        self.inky_display.set_image(self.img)
        self.inky_display.show()
