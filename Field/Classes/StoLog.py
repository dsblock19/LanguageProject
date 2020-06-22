class StoConversion:

    def __init__(self):
        pass

    #Build New Family
    def InSto():
        #LIBRARIES
        from inky import InkyWHAT
        from PIL import Image, ImageFont, ImageDraw

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

        stof = open('/home/pi/LanguageProject/Output/StoLog.txt', 'a')
        stof.write('\n' + root)
        stof.close()

        stomessage = root
        x = 0
        y = 100
        draw.text((x, y), stomessage, inky_display.RED, stofont)
        #flipped = img.rotate(90)
        #inky_display.set_image(flipped)
        inky_display.set_image(img)
        inky_display.show()
