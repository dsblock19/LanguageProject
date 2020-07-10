#LIBRARIES
import random
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw


class WordGen():

    def __init__(self):
        #SETUP
        # screen
        self.inky_display = InkyWHAT("red")
        self.inky_display.set_border(self.inky_display.WHITE)
        #img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        self.img = Image.new("P", (400, 300))
        self.draw = ImageDraw.Draw(self.img)
        self.stofontpath = '/home/pi/LanguageProject/Field/Classes/Fonts/sto-ith/sto-ith.ttf'
        self.stofont = ImageFont.truetype(self.stofontpath, 41)
        self.x = 50
        self.y = -67

        # avalible sounds in language
        self.core_consonants = [ 'd', 't', 'k', 'z', 'n', 's', 'm', 'g', 'p', 'v', 'j', 'b', 'h', 'r' ]
        self.core_vowels = [ 'aw', 'o', 'u', 'a', 'oo', 'e' ]
        self.other_vowels = [ 'i:i', 'i' ]
        self.other_consonants = [ 'c', 'sh', 'th', 'st', 'ch', 'x' ]
        self.other_c = [ 'qua' ]
        self.all_vowels = self.core_vowels + self.other_vowels
        self.all_consonants = self.core_consonants + self.other_consonants
        self.allsounds = self.core_consonants + self.core_vowels + self.other_vowels + self.other_consonants
        self.allcategories = [self.core_consonants, self.core_vowels, self.other_vowels, self.other_consonants,
                        self.other_c, self.all_vowels, self.all_consonants, self.allsounds
                        ]
        #Word Class
        self.RV = ['t']
        self.NI = [ 'i:i', 'aw', 'a' ]
        self.NII = [ 'c', 'k', 'x' ]
        self.NIII = [ 'st', 'th' ]
        self.NIV = [ 'ms', 'm', 'i' ]
        self.NV = [ 'o', 'e', 'ipa' ]
        self.NVI = [ 'd', 'z', 'n', 'g', 'p', 'b' ]
        self.WClass = [self.RV, self.NI, self.NII, self.NIII, self.NIV, self.NV, self.NVI]

        #Root Families
        self.holy = ['daw', 'do']
        self.building = [ 'tan', 'tam' ]
        self.domanimal = [ 'go', 'ox', 'awx' ]
        self.stone = [ 'ie', 'ist' ]
        self.forest = [ 'he', 'haw' ]
        self.water = [ 'ipi', 'ipa' ]
        self.atoms = [ 'po', 'oaw' ]
        self.thebody = [ 'shu', 'sheaw', 'eu' ]
        self.writing = 'sto'
        self.human = 'uc'
        self.health = 'pi'
        self.evil =  [ 'awm', 'im' ]
        self.salt = 'so'

        #Comparison Families
        self.like = 'oo'
        self.state = 'ca'
        self.Comfam = [self.like, self.state]

    #Build New Family
    def NewFam(self):
        family = input('\nFamilies: ')
        root = ''
        family = family.upper()
        if family == '':
            rt1 = random.choice(self.allcategories[0]) + random.choice(self.allcategories[1])
            rt2 = random.choice(self.allcategories[1]) + random.choice(self.allcategories[1])
            rt3 = random.choice(self.allcategories[1]) + random.choice(self.allcategories[0])
            rttup = (rt1, rt2, rt3)
            root = random.choice(rttup)
        #Families
        if 'HOLY' in family:
            root = root + random.choice(self.holy)
        if 'HUMAN' in family:
            root = root + self.human
        if 'WRITING' in family:
            root = root + self.writing
        if 'HEALTH' in family:
            root = root + self.health
        if 'THE BODY' in family:
            root = root + random.choice(self.thebody)
        if 'DOMESTIC ANIMALS' in family:
            root = root + random.choice(self.domanimal)
        if 'ATOMS' in family:
            root = root + random.choice(self.atoms)
        if 'WATER' in family:
            root = root + random.choice(self.water)
        if 'STONE' in family:
            root = root + random.choice(self.stone)
        if 'FOREST' in family:
            root = root + random.choice(self.forest)
        if 'BUILDING' in family:
            root = root + random.choice(self.building)
        if 'SALT' in family:
            root = root + self.salt
        if 'EVIL' in family:
            root = root + random.choice(self.evil)
        else:
            rt1 = random.choice(self.allcategories[0]) + random.choice(self.allcategories[1])
            rt2 = random.choice(self.allcategories[1]) + random.choice(self.allcategories[1])
            rt3 = random.choice(self.allcategories[1]) + random.choice(self.allcategories[0])
            rttup = (rt1, rt2, rt3)
            root = random.choice(rttup)

        #Class
        #I
        if root[-1] in ['o', 'i', 'u', 'oo']:
            NI = root + random.choice(self.allcategories[0]) + random.choice(self.WClass[1])
        elif root[-1] in ['i:i']:
            noEE = ['aw', 'a']
            NI = root + random.choice(noEE)
        elif root[-1] in ['aw']:
            noAW = ['i:i', 'a']
            NI = root + random.choice(noAW)
        elif root[-1] in ['a']:
            noA = ['aw', 'i:i']
            NI = root + random.choice(noA)
        else:
            NI = root + random.choice(self.WClass[1])

        #II
        if root[-1] in ['d', 't', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'th', 'st', 'v', 'j', 'ch', 'b','h', 'r' ]:
            NII = root + random.choice(self.allcategories[1]) + random.choice(self.WClass[2])
        elif root[-1] in ['c']:
            noC= ['k', 'x']
            NII = root + random.choice(noC)
        elif root[-1] in ['k']:
            noK = ['c', 'x']
            NII = root + random.choice(noK)
        elif root[-1] in ['x']:
            noX = ['c', 'k']
            NII = root + random.choice(noX)
        else:
            NII = root + random.choice(self.WClass[2])

        #III
        if root[-1] in ['c', 'k', 'x', 'd', 't', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r' ]:
            NIII = root + random.choice(self.allcategories[1]) + random.choice(self.WClass[3])
        elif root[-1] in ['st']:
            noST = ['th']
            NIII = root + random.choice(noST)
        elif root[-1] in ['th']:
            noTH = ['st']
            NIII = root + random.choice(noTH)
        else:
            NIII = root + random.choice(self.WClass[3])

        #IV
        if root[-1] in [ 'o', 'e', 'i', 'u', 'oo', 'i:i', 'aw', 'a']:
            noi = ['ms', 'm']
            NIV = root + random.choice(self.allcategories[1])+ random.choice(noi)
        elif root[-1] in ['c', 'k', 'x', 'd', 't', 'z', 'n', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b', 'h', 'r' ]:
            NIV = root + random.choice(self.allcategories[0]) + 'i'
        elif root[-1] in ['ms']:
            noMS = ['m', 'i']
            NIV = root + random.choice(noMS)
        elif root[-1] in ['m']:
            noM = ['ms', 'i']
            NIV = root + random.choice(noM)
        elif root[-1] in ['i']:
            noI = ['ms', 'm']
            NIV = root + random.choice(noI)
        else:
            NIV = root + random.choice(self.WClass[4])

        #V
        if root[-1] in [ 'i', 'u', 'oo', 'i:i', 'aw', 'a']:
            NV = root + random.choice(self.allcategories[0]) + random.choice(self.WClass[5])
        elif root[-1] in ['o']:
            noO = ['e', 'ipa']
            NV = root + random.choice(noO)
        elif root[-1] in ['e']:
            noE = ['o', 'ipa']
            NV = root + random.choice(noE)
        elif root[-1] in ['ipa']:
            noIPA = ['o', 'e']
            NV = root + random.choice(noIPA)
        else:
            NV = root + random.choice(self.WClass[5])

        #V
        if root[-1] in ['t', 'st', 'th', 'c', 'k', 'x', 'd', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r']:
            V = root + random.choice(self.allcategories[1]) + random.choice(self.WClass[0])
        else:
            V = root +random.choice(self.WClass[0])

        #Make Upper Case
        root = root.upper()
        Verbs = V.upper()
        NounsI = NI.upper()
        NounsII = NII.upper()
        NounsIII = NIII.upper()
        NounsIV = NIV.upper()
        NounsV = NV.upper()
        #Font Specific Change
        #ST --> F
        root = root.replace('ST', 'F')
        Verbs = Verbs.replace('ST', 'F')
        NounsI = NounsI.replace('ST', 'F')
        NounsII = NounsII.replace('ST', 'F')
        NounsIII = NounsIII.replace('ST', 'F')
        NounsIV = NounsIV.replace('ST', 'F')
        NounsV = NounsV.replace('ST', 'F')
        #OO --> L
        core = root.replace('OO', 'L')
        Verbs = Verbs.replace('OO', 'L')
        NounsI = NounsI.replace('OO', 'L')
        NounsII = NounsII.replace('OO', 'L')
        NounsIII = NounsIII.replace('OO', 'L')
        NounsIV = NounsIV.replace('OO', 'L')
        NounsV = NounsV.replace('OO', 'L')
        #SH --> Q
        root = root.replace('SH', 'Q')
        Verbs = Verbs.replace('SH', 'Q')
        NounsI = NounsI.replace('SH', 'Q')
        NounsII = NounsII.replace('SH', 'Q')
        NounsIII = NounsIII.replace('SH', 'Q')
        NounsIV = NounsIV.replace('SH', 'Q')
        NounsV = NounsV.replace('SH', 'Q')
        #AW --> W
        root = root.replace('AW', 'W')
        Verbs = Verbs.replace('AW', 'W')
        NounsI = NounsI.replace('AW', 'W')
        NounsII = NounsII.replace('AW', 'W')
        NounsIII = NounsIII.replace('AW', 'W')
        NounsIV = NounsIV.replace('AW', 'W')
        NounsV = NounsV.replace('AW', 'W')
        #I:I --> Y
        root = root.replace('I:I', 'Y')
        Verbs = Verbs.replace('I:I', 'Y')
        NounsI = NounsI.replace('I:I', 'Y')
        NounsII = NounsII.replace('I:I', 'Y')
        NounsIII = NounsIII.replace('I:I', 'Y')
        NounsIV = NounsIV.replace('I:I', 'Y')
        NounsV = NounsV.replace('I:I', 'Y')
        #CH --> @
        root = root.replace('CH', '@')
        Verbs = Verbs.replace('CH', '@')
        NounsI = NounsI.replace('CH', '@')
        NounsII = NounsII.replace('CH', '@')
        NounsIII = NounsIII.replace('CH', '@')
        NounsIV = NounsIV.replace('CH', '@')
        NounsV = NounsV.replace('CH', '@')
        #TH --> #
        root = root.replace('TH', '#')
        Verbs = Verbs.replace('TH', '#')
        NounsI = NounsI.replace('TH', '#')
        NounsII = NounsII.replace('TH', '#')
        NounsIII = NounsIII.replace('TH', '#')
        NounsIV = NounsIV.replace('TH', '#')
        NounsV = NounsV.replace('TH', '#')

        #Log Results
        f = open('/home/pi/LanguageProject/Output/RandomFamily.txt', 'a')
        f.write('\n\n[Root: ' + root + '] Verb: ' + V + '\n')
        f.write('   NounI: ' + NI + '\n NounII: ' + NII + '\n   NounIII: ' + NIII + '\n NounIV: ' + NIV + '\n   NounV: ' + NV)
        f.close()
        stof = open('/home/pi/LanguageProject/Output/StoIthRandomFamily.txt', 'a')
        stof.write('\n\n[Root: ' + root + '] Verb: ' + Verbs + '\n')
        stof.write('   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV)
        stof.close()

        '''
        #Print Results
        print('\nIn Sto:\n[Root: ' + root + '] Verb: ' + Verbs)
        print('   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV)
        '''
        #NIfam
        NIfam = ''
        if self.holy[0] in NI or self.holy[1] in NI:
            NIfam = NIfam + ' Holy'
        if self.building[0] in NI or self.building[1] in NI:
            NIfam = NIfam + ' Building'
        if self.domanimal[0] in NI or self.domanimal[1] in NI or self.domanimal[2] in NI:
            NIfam = NIfam + ' Domestic-Animal'
        if self.stone[0] in NI or self.stone[1] in NI:
            NIfam = NIfam + ' Stone'
        if self.forest[0] in NI or self.forest[1] in NI:
            NIfam = NIfam + ' Forest'
        if self.water[0] in NI or self.water[1] in NI:
            NIfam = NIfam + ' Water'
        if self.atoms[0] in NI or self.atoms[1] in NI:
            NIfam = NIfam + ' Atoms'
        if self.thebody[0] in NI or self.thebody[1] in NI or self.thebody[2] in NI:
            NIfam = NIfam + ' The-Body'
        if self.writing in NI:
            NIfam = NIfam + ' Writing'
        if self.human in NI:
            NIfam = NIfam + ' Human'
        if self.health in NI:
            NIfam = NIfam + ' Health'
        if self.evil[0] in NI or self.evil[1] in NI:
            NIfam = NIfam + ' Evil'
        if self.salt in NI:
            NIfam = NIfam + ' Salt'
        #NIIfam
        NIIfam = ''
        if self.holy[0] in NII or self.holy[1] in NII:
            NIIfam = NIIfam + ' Holy'
        if self.building[0] in NII or self.building[1] in NII:
            NIIfam = NIIfam + ' Building'
        if self.domanimal[0] in NII or self.domanimal[1] in NII or self.domanimal[2] in NII:
            NIIfam = NIIfam + ' Domestic-Animal'
        if self.stone[0] in NII or self.stone[1] in NII:
            NIIfam = NIIfam + ' Stone'
        if self.forest[0] in NII or self.forest[1] in NII:
            NIIfam = NIIfam + ' Forest'
        if self.water[0] in NII or self.water[1] in NII:
            NIIfam = NIIfam + ' Water'
        if self.atoms[0] in NII or self.atoms[1] in NII:
            NIIfam = NIIfam + ' Atoms'
        if self.thebody[0] in NII or self.thebody[1] in NII or self.thebody[2] in NII:
            NIIfam = NIIfam + ' The-Body'
        if self.writing in NII:
            NIIfam = NIIfam + ' Writing'
        if self.human in NII:
            NIIfam = NIIfam + ' Human'
        if self.health in NII:
            NIIfam = NIIfam + ' Health'
        if self.evil[0] in NII or self.evil[1] in NII:
            NIIfam = NIIfam + ' Evil'
        if self.salt in NII:
            NIIfam = NIIfam + ' Salt'
        #NIIIfam
        NIIIfam = ''
        if self.holy[0] in NIII or self.holy[1] in NIII:
            NIIIfam = NIIIfam + ' Holy'
        if self.building[0] in NIII or self.building[1] in NIII:
            NIIIfam = NIIIfam + ' Building'
        if self.domanimal[0] in NIII or self.domanimal[1] in NIII or self.domanimal[2] in NIII:
            NIIIfam = NIIIfam + ' Domestic-Animal'
        if self.stone[0] in NIII or self.stone[1] in NIII:
            NIIIfam = NIIIfam + ' Stone'
        if self.forest[0] in NIII or self.forest[1] in NIII:
            NIIIfam = NIIIfam + ' Forest'
        if self.water[0] in NIII or self.water[1] in NIII:
            NIIIfam = NIIIfam + ' Water'
        if self.atoms[0] in NIII or self.atoms[1] in NIII:
            NIIIfam = NIIIfam + ' Atoms'
        if self.thebody[0] in NIII or self.thebody[1] in NIII or self.thebody[2] in NIII:
            NIIIfam = NIIIfam + ' The-Body'
        if self.writing in NIII:
            NIIIfam = NIIIfam + ' Writing'
        if self.human in NIII:
            NIIIfam = NIIIfam + ' Human'
        if self.health in NIII:
            NIIIfam = NIIIfam + ' Health'
        if self.evil[0] in NIII or self.evil[1] in NIII:
            NIIIfam = NIIIfam + ' Evil'
        if self.salt in NIII:
            NIIIfam = NIIIfam + ' Salt'
        #NIVfam
        NIVfam = ''
        if self.holy[0] in NIV or self.holy[1] in NIV:
            NIVfam = NIVfam + ' Holy'
        if self.building[0] in NIV or self.building[1] in NIV:
            NIVfam = NIVfam + ' Building'
        if self.domanimal[0] in NIV or self.domanimal[1] in NIV or self.domanimal[2] in NIV:
            NIVfam = NIVfam + ' Domestic-Animal'
        if self.stone[0] in NIV or self.stone[1] in NIV:
            NIVfam = NIVfam + ' Stone'
        if self.forest[0] in NIV or self.forest[1] in NIV:
            NIVfam = NIVfam + ' Forest'
        if self.water[0] in NIV or self.water[1] in NIV:
            NIVfam = NIVfam + ' Water'
        if self.atoms[0] in NIV or self.atoms[1] in NIV:
            NIVfam = NIVfam + ' Atoms'
        if self.thebody[0] in NIV or self.thebody[1] in NIV or self.thebody[2] in NI:
            NIVfam = NIVfam + ' The-Body'
        if self.writing in NIV:
            NIVfam = NIVfam + ' Writing'
        if self.human in NIV:
            NIVfam = NIVfam + ' Human'
        if self.health in NIV:
            NIVfam = NIVfam + ' Health'
        if self.evil[0] in NIV or self.evil[1] in NIV:
            NIVfam = NIVfam + ' Evil'
        if self.salt in NIV:
            NIVfam = NIVfam + ' Salt'
        #NVfam
        NVfam = ''
        if self.holy[0] in NV or self.holy[1] in NV:
            NVfam = NVfam + ' Holy'
        if self.building[0] in NV or self.building[1] in NV:
            NVfam = NVfam + ' Building'
        if self.domanimal[0] in NV or self.domanimal[1] in NV or self.domanimal[2] in NV:
            NVfam = NVfam + ' Domestic-Animal'
        if self.stone[0] in NV or self.stone[1] in NV:
            NVfam = NVfam + ' Stone'
        if self.forest[0] in NV or self.forest[1] in NV:
            NVfam = NVfam + ' Forest'
        if self.water[0] in NV or self.water[1] in NV:
            NVfam = NVfam + ' Water'
        if self.atoms[0] in NV or self.atoms[1] in NV:
            NVfam = NVfam + ' Atoms'
        if self.thebody[0] in NV or self.thebody[1] in NV or self.thebody[2] in NV:
            NVfam = NVfam + ' The-Body'
        if self.writing in NV:
            NVfam = NVfam + ' Writing'
        if self.human in NV:
            NVfam = NVfam + ' Human'
        if self.health in NV:
            NVfam = NVfam + ' Health'
        if self.evil[0] in NV or self.evil[1] in NV:
            NVfam = NVfam + ' Evil'
        if self.salt in NV:
            NVfam = NVfam + ' Salt'

        print('\nRegular:\n[Root: ' + root + '] Verb: ' + V)
        print('   NounI: ' + NI + ' | Fam:' + NIfam + '\n NounII: ' + NII + '  | Fam:' + NIIfam + '\n   NounIII: ' + NIII + ' | Fam:' + NIIIfam)
        print('NounIV: ' + NIV + ' | Fam:' + NIVfam + '\n   NounV: ' + NV + ' | Fam:' + NVfam)
        print('')

        stomessage = '\n' + NounsI + '\n ' + NounsII + '\n   ' + NounsIII + '\n  ' + NounsIV + '\n   ' + NounsV

        eink = input('Inky? ')
        eink = eink.upper()
        if eink == 'YES':
            self.inky_display.show(self.inky_display.Image.new('P', (400, 300)))
            self.draw.text((self.x, self.y), stomessage, self.inky_display.RED, self.stofont)
            #flipped = img.rotate(90)
            #inky_display.set_image(flipped)
            self.inky_display.set_border(self.inky_display.WHITE)
            self.inky_display.set_image(self.img)
            self.inky_display.show()
        print('')
