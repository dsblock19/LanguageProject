#Libraries
import random
import pymysql
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

class SQLint():

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

    def WordDef(self):
        print('')
        word = input('Word: ')
        generation = input('Generation: ')
        if word == '':
            results = []
            if generation == 'I':
                sql = "SELECT * FROM FoundationalFamilies;"
            elif generation == 'II':
                sql = "SELECT * FROM GenerationII;"
            #with self.con:
            try:
                self.cur.execute(sql)
                results = self.cur.fetchall()
                self.con.commit()
                for i in range(len(results)):
                    print(results[i])
                print(str(len(results)))
            except Exception as e:
                self.con.rollback()
                print(e)
        else:
            if generation == 'I':
                sql = "SELECT ALL * FROM FoundationalFamilies WHERE word = '" + word + "';"
            elif generation == 'II':
                sql = "SELECT ALL * FROM GenerationII WHERE word = '" + word + "';"
            #with self.con:
            try:
                self.cur.execute(sql)
                results = self.cur.fetchall()
                self.con.commit()
                for i in range(len(results)):
                    print(results[i])
                root = str(word)
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

class WordCreation():

    def __init__(self):
        #SETUP
        # screen
        self.inky_display = InkyWHAT("black")
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
        if family == '':
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
            self.img = Image.new("P", (400, 300))
            self.draw = ImageDraw.Draw(self.img)
            self.draw.text((self.x, self.y), stomessage, self.inky_display.RED, self.stofont)
            self.inky_display.set_border(self.inky_display.WHITE)
            self.inky_display.set_image(self.img)
            self.inky_display.show()
        print('')

    def CustNewFam(self):
        sounds = input('\nRoot Sounds: ')
        root = ''
        if sounds == '':
            rt1 = random.choice(self.allcategories[0]) + random.choice(self.allcategories[1])
            rt2 = random.choice(self.allcategories[1]) + random.choice(self.allcategories[1])
            rt3 = random.choice(self.allcategories[1]) + random.choice(self.allcategories[0])
            rttup = (rt1, rt2, rt3)
            root = random.choice(rttup)
        else:
            rt1 = sounds + random.choice(self.allcategories[0]) + random.choice(self.allcategories[1])
            rt2 = sounds + random.choice(self.allcategories[1]) + random.choice(self.allcategories[1])
            rt3 = sounds + random.choice(self.allcategories[1]) + random.choice(self.allcategories[0])
            rt4 = random.choice(self.allcategories[0]) + sounds + random.choice(self.allcategories[1])
            rt5 = random.choice(self.allcategories[1]) + sounds + random.choice(self.allcategories[1])
            rt6 = random.choice(self.allcategories[1]) + sounds + random.choice(self.allcategories[0])
            rt7 = random.choice(self.allcategories[0]) + random.choice(self.allcategories[1]) + sounds
            rt8 = random.choice(self.allcategories[1]) + random.choice(self.allcategories[1]) + sounds
            rt9 = random.choice(self.allcategories[1]) + random.choice(self.allcategories[0]) + sounds
            rt10 = sounds
            rttup = (rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10)
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
            self.img = Image.new("P", (400, 300))
            self.draw = ImageDraw.Draw(self.img)

            self.draw.text((self.x, self.y), stomessage, self.inky_display.RED, self.stofont)
            #flipped = img.rotate(90)
            #inky_display.set_image(flipped)
            self.inky_display.set_border(self.inky_display.WHITE)
            self.inky_display.set_image(self.img)
            self.inky_display.show()
        print('')

class inkyOnly():

    def __init__(self):
        # screen
        self.inky_display = InkyWHAT("black")
        self.inky_display.set_border(self.inky_display.WHITE)
        #img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        self.img = Image.new("P", (400, 300))
        self.draw = ImageDraw.Draw(self.img)
        self.stofontpath = '/home/pi/LanguageProject/Field/Classes/Fonts/sto-ith/sto-ith.ttf'
        self.stofont = ImageFont.truetype(self.stofontpath, 50)
        self.x = 0
        self.y = 0

        #self.root = 'dtkznsm\ngpvjbhr\nawouaooei:i\nicshthstchx'
        self.root = 'dtnawi:ieu\naiooozcch\nhkstshmpg\nxsvthbrj'

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
        self.inky_display.set_border(self.inky_display.WHITE)
        self.inky_display.set_image(self.img)
        self.inky_display.show()

        print('')

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
        print('')

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
