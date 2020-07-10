#Libraries
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

class ConjugateVerb():

    def __init__(self):
        #Setup
        #I/He/She/They(sing.), You, Ya'll/Them/They(plur), We(royal), We(exclusive)
        self.PresEndings = [ 'aj','ast','asta','am','ama' ]
        self.PastEndings = [ 'a','as','asa','an','ana' ]
        self.FutureEndings = [ 'ua','ue','ust','un','una' ]
        self.PresProgEndings = [ 'aja','asta','ast','ama','am' ]
        self.PastProgEndings = [ 'ag','asa','as','ana','an' ]
        self.FutureProgEndings = [ 'ui','ust','ue','una','un' ]
        self.O = 'I/He/She/They(sing): '
        self.I = 'You: '
        self.II = "Ya'll/Them/They(plur): "
        self.III = 'We(royal): '
        self.IV = 'We(exclusive): '

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


    def Conjugate(self):
        print('')
        verb = input('Verb: ')
        tense = input(' Tense: ')
        print('')
        print('Verb: ' + str(verb) + ' | Tense: ' + str(tense))
        tense = tense.upper()
        if 'PRESENT' in tense:
            print(self.O + verb + self.PresEndings[0])
            print(self.I + verb + self.PresEndings[1])
            print(self.II + verb + self.PresEndings[2])
            print(self.III + verb + self.PresEndings[3])
            print(self.IV + verb + self.PresEndings[4])
        elif 'PAST' in tense:
            print(self.O + verb + self.PastEndings[0])
            print(self.I + verb + self.PastEndings[1])
            print(self.II + verb + self.PastEndings[2])
            print(self.III + verb + self.PastEndings[3])
            print(self.IV + verb + self.PastEndings[4])
        elif 'FUTURE' in tense:
            print(self.O + verb + self.FutureEndings[0])
            print(self.I + verb + self.FutureEndings[1])
            print(self.II + verb + self.FutureEndings[2])
            print(self.III + verb + self.FutureEndings[3])
            print(self.IV + verb + self.FutureEndings[4])
        elif 'PRESENT PROGRESSIVE' in tense:
            print(self.O + verb + self.PresProgEndings[0])
            print(self.I + verb + self.PresProgEndings[1])
            print(self.II + verb + self.PresProgEndings[2])
            print(self.III + verb + self.PresProgEndings[3])
            print(self.IV + verb + self.PresProgEndings[4])
        elif 'PAST PROGRESSIVE' in tense:
            print(self.O + verb + self.PastProgEndings[0])
            print(self.I + verb + self.PastProgEndings[1])
            print(self.II + verb + self.PastProgEndings[2])
            print(self.III + verb + self.PastProgEndings[3])
            print(self.IV + verb + self.PastProgEndings[4])
        elif 'FUTURE PROGRESSIVE' in tense:
            print(self.O + verb + self.FutureProgEndings[0])
            print(self.I + verb + self.FutureProgEndings[1])
            print(self.II + verb + self.FutureProgEndings[2])
            print(self.III + verb + self.FutureProgEndings[3])
            print(self.IV + verb + self.FutureProgEndings[4])
        print('')
        root = str(verb)
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

        self.draw.text((self.x, self.y), root, self.inky_display.RED, self.stofont)
        #flipped = img.rotate(90)
        #inky_display.set_image(flipped)
        self.inky_display.set_border(self.inky_display.WHITE)
        self.inky_display.set_image(self.img)
        self.inky_display.show()
