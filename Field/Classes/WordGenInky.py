class WordGen:

    def __init__(self):
        pass

    #Build New Family
    def NewFam():
        #LIBRARIES
        import random
        from inky import InkyWHAT
        from PIL import Image, ImageFont, ImageDraw

        #SETUP
        # screen
        inky_display = InkyWHAT("red")
        inky_display.set_border(inky_display.WHITE)
        #img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        img = Image.new("P", (400, 300))
        draw = ImageDraw.Draw(img)
        fontpath = '/home/pi/LanguageProject/Field/Classes/Fonts/CourierNewFett.ttf'
        stofontpath = '/home/pi/LanguageProject/Field/Classes/Fonts/sto-ith/sto-ith.ttf'
        stofont = ImageFont.truetype(stofontpath, 36)
        font = ImageFont.truetype(fontpath, 20)
        # avalible sounds in language
        core_consonants = ( 'd', 't', 'k', 'z', 'n', 's', 'm', 'g', 'p', 'v', 'j', 'b', 'h', 'r' )
        core_vowels = ( 'aw', 'o', 'u', 'a', 'oo', 'e' )
        other_vowels = ( 'i:i', 'i' )
        other_consonants = ( 'c', 'sh', 'th', 'st', 'ch', 'x' )
        other_c = ( 'qua' )
        all_vowels = core_vowels + other_vowels
        all_consonants = core_consonants + other_consonants
        allsounds = core_consonants + core_vowels + other_vowels + other_consonants
        allcategories = (core_consonants, core_vowels, other_vowels, other_consonants,
                        other_c, all_vowels, all_consonants, allsounds
                        )

        #Word Class
        RV = ('t')
        NI = ( 'i:i', 'aw', 'a' )
        NII = ( 'c', 'k', 'x' )
        NIII = ( 'st', 'th' )
        NIV = ( 'ms', 'm', 'i' )
        NV = ( 'o', 'e', 'ipa' )
        NVI = ( 'd', 'z', 'n', 'g', 'p', 'b' )
        WClass = (RV, NI, NII, NIII, NIV, NV, NVI)

        #Root Families
        holy = ('daw', 'do')
        building = ('tan', 'tam')
        domanimal = ('go', 'ox', 'awx')
        stone = ('ie', 'ist')
        forest = ('he', 'haw')
        water = 'ipi'
        atoms = ('po', 'oaw')
        thebody = ('shu', 'sheaw', 'eu')
        writing = 'sto'
        human = 'uc'
        health = 'pi'
        evil = ('awm', 'im')
        Rfam = (holy, building, domanimal, stone, forest, water,
                atoms, thebody, writing, human, health, evil
                )

        #Comparison Families
        like = 'oo'
        state = 'ca'
        Comfam = (like, state)

        family = input('\nFamily: ')
        if family == 'None':
            rt1 = random.choice(allcategories[0]) + random.choice(allcategories[1])
            rt2 = random.choice(allcategories[1]) + random.choice(allcategories[1])
            rt3 = random.choice(allcategories[1]) + random.choice(allcategories[0])
            rttup = (rt1, rt2, rt3)
            root = random.choice(rttup)
        #Families
        elif family == 'Holy':
            root = random.choice(Rfam[0])
        elif family == 'Building':
            root = random.choice(Rfam[1])
        elif family == 'Demoestic Animal':
            root = random.choice(Rfam[2])
        elif family == 'Stone':
            root = random.choice(Rfam[3])
        elif family == 'Forest':
            root = random.choice(Rfam[4])
        elif family == 'Water':
            root = random.choice(Rfam[5])
        elif family == 'Atoms':
            root = random.choice(Rfam[6])
        elif family == 'The Body':
            root = random.choice(Rfam[7])
        elif family == 'Writing':
            root = random.choice(Rfam[8])
        elif family == 'Human':
            root = random.choice(Rfam[9])
        elif family == 'Health':
            root = random.choice(Rfam[10])
        elif family == 'Evil':
            root = random.choice(Rfam[11])
        else:
            rt1 = random.choice(allcategories[0]) + random.choice(allcategories[1])
            rt2 = random.choice(allcategories[1]) + random.choice(allcategories[1])
            rt3 = random.choice(allcategories[1]) + random.choice(allcategories[0])
            rttup = (rt1, rt2, rt3)
            root = random.choice(rttup)

        #Class
        if root[-1] in ['o', 'i', 'u', 'oo']:
            NI = root + random.choice(allcategories[0]) + random.choice(WClass[1])
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
            NI = root + random.choice(WClass[1])

        if root[-1] in ['d', 't', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'th', 'st', 'v', 'j', 'ch', 'b','h', 'r' ]:
            NII = root + random.choice(allcategories[1]) + random.choice(WClass[2])
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
            NII = root + random.choice(WClass[2])

        if root[-1] in ['c', 'k', 'x', 'd', 't', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r' ]:
            NIII = root + random.choice(allcategories[1]) + random.choice(WClass[3])
        elif root[-1] in ['st']:
            noST = ['th']
            NIII = root + random.choice(noST)
        elif root[-1] in ['th']:
            noTH = ['st']
            NIII = root + random.choice(noTH)
        else:
            NIII = root + random.choice(WClass[3])

        if root[-1] in [ 'o', 'e', 'i', 'u', 'oo', 'i:i', 'aw', 'a']:
            noi = ['ms', 'm']
            NIV = root + random.choice(allcategories[1])+ random.choice(noi)
        elif root[-1] in ['c', 'k', 'x', 'd', 't', 'z', 'n', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b', 'h', 'r' ]:
            NIV = root + random.choice(allcategories[0]) + 'i'
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
            NIV = root + random.choice(WClass[4])

        if root[-1] in [ 'i', 'u', 'oo', 'i:i', 'aw', 'a']:
            NV = root + random.choice(allcategories[0]) + random.choice(WClass[5])
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
            NV = root + random.choice(WClass[5])

        if root[-1] in ['t', 'st', 'th', 'c', 'k', 'x', 'd', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r']:
            V = root + random.choice(allcategories[1]) + WClass[0]
        else:
            V = root + WClass[0]

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

        #Print Results
        print('\nIn Sto:\n[Root: ' + root + '] Verb: ' + Verbs)
        print('   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV)
        #NIfam
        NIfam = ''
        if holy[0] in NI or holy[1] in NI:
            NIfam = NIfam + ' Holy'
        if building[0] in NI or building[1] in NI:
            NIfam = NIfam + ' Building'
        if domanimal[0] in NI or domanimal[1] in NI or domanimal[2] in NI:
            NIfam = NIfam + ' Domestic-Animal'
        if stone[0] in NI or stone[1] in NI:
            NIfam = NIfam + ' Stone'
        if forest[0] in NI or forest[1] in NI:
            NIfam = NIfam + ' Forest'
        if water in NI:
            NIfam = NIfam + ' Water'
        if atoms[0] in NI or atoms[1] in NI:
            NIfam = NIfam + ' Atoms'
        if thebody[0] in NI or thebody[1] in NI or thebody[2] in NI:
            NIfam = NIfam + ' The-Body'
        if writing in NI:
            NIfam = NIfam + ' Writing'
        if human in NI:
            NIfam = NIfam + ' Human'
        if health in NI:
            NIfam = NIfam + ' Health'
        if evil[0] in NI or evil[1] in NI:
            NIfam = NIfam + ' Evil'
        #NIIfam
        NIIfam = ''
        if holy[0] in NII or holy[1] in NII:
            NIIfam = NIIfam + ' Holy'
        if building[0] in NII or building[1] in NII:
            NIIfam = NIIfam + ' Building'
        if domanimal[0] in NII or domanimal[1] in NII or domanimal[2] in NII:
            NIIfam = NIIfam + ' Domestic-Animal'
        if stone[0] in NII or stone[1] in NII:
            NIIfam = NIIfam + ' Stone'
        if forest[0] in NII or forest[1] in NII:
            NIIfam = NIIfam + ' Forest'
        if water in NII:
            NIIfam = NIIfam + ' Water'
        if atoms[0] in NII or atoms[1] in NII:
            NIIfam = NIIfam + ' Atoms'
        if thebody[0] in NII or thebody[1] in NII or thebody[2] in NII:
            NIIfam = NIIfam + ' The-Body'
        if writing in NII:
            NIIfam = NIIfam + ' Writing'
        if human in NII:
            NIIfam = NIIfam + ' Human'
        if health in NII:
            NIIfam = NIIfam + ' Health'
        if evil[0] in NII or evil[1] in NII:
            NIIfam = NIIfam + ' Evil'
        #NIIIfam
        NIIIfam = ''
        if holy[0] in NIII or holy[1] in NIII:
            NIIIfam = NIIIfam + ' Holy'
        if building[0] in NIII or building[1] in NIII:
            NIIIfam = NIIIfam + ' Building'
        if domanimal[0] in NIII or domanimal[1] in NIII or domanimal[2] in NIII:
            NIIIfam = NIIIfam + ' Domestic-Animal'
        if stone[0] in NIII or stone[1] in NIII:
            NIIIfam = NIIIfam + ' Stone'
        if forest[0] in NIII or forest[1] in NIII:
            NIIIfam = NIIIfam + ' Forest'
        if water in NIII:
            NIIIfam = NIIIfam + ' Water'
        if atoms[0] in NIII or atoms[1] in NIII:
            NIIIfam = NIIIfam + ' Atoms'
        if thebody[0] in NIII or thebody[1] in NIII or thebody[2] in NIII:
            NIIIfam = NIIIfam + ' The-Body'
        if writing in NIII:
            NIIIfam = NIIIfam + ' Writing'
        if human in NIII:
            NIIIfam = NIIIfam + ' Human'
        if health in NIII:
            NIIIfam = NIIIfam + ' Health'
        if evil[0] in NIII or evil[1] in NIII:
            NIIIfam = NIIIfam + ' Evil'
        #NIVfam
        NIVfam = ''
        if holy[0] in NIV or holy[1] in NIV:
            NIVfam = NIVfam + ' Holy'
        if building[0] in NIV or building[1] in NIV:
            NIVfam = NIVfam + ' Building'
        if domanimal[0] in NIV or domanimal[1] in NIV or domanimal[2] in NIV:
            NIVfam = NIVfam + ' Domestic-Animal'
        if stone[0] in NIV or stone[1] in NIV:
            NIVfam = NIVfam + ' Stone'
        if forest[0] in NIV or forest[1] in NIV:
            NIVfam = NIVfam + ' Forest'
        if water in NIV:
            NIVfam = NIVfam + ' Water'
        if atoms[0] in NIV or atoms[1] in NIV:
            NIVfam = NIVfam + ' Atoms'
        if thebody[0] in NIV or thebody[1] in NIV or thebody[2] in NI:
            NIVfam = NIVfam + ' The-Body'
        if writing in NIV:
            NIVfam = NIVfam + ' Writing'
        if human in NIV:
            NIVfam = NIVfam + ' Human'
        if health in NIV:
            NIVfam = NIVfam + ' Health'
        if evil[0] in NIV or evil[1] in NIV:
            NIVfam = NIVfam + ' Evil'
        #NVfam
        NVfam = ''
        if holy[0] in NV or holy[1] in NV:
            NVfam = NVfam + ' Holy'
        if building[0] in NV or building[1] in NV:
            NVfam = NVfam + ' Building'
        if domanimal[0] in NV or domanimal[1] in NV or domanimal[2] in NV:
            NVfam = NVfam + ' Domestic-Animal'
        if stone[0] in NV or stone[1] in NV:
            NVfam = NVfam + ' Stone'
        if forest[0] in NV or forest[1] in NV:
            NVfam = NVfam + ' Forest'
        if water in NV:
            NVfam = NVfam + ' Water'
        if atoms[0] in NV or atoms[1] in NV:
            NVfam = NVfam + ' Atoms'
        if thebody[0] in NV or thebody[1] in NV or thebody[2] in NV:
            NVfam = NVfam + ' The-Body'
        if writing in NV:
            NVfam = NVfam + ' Writing'
        if human in NV:
            NVfam = NVfam + ' Human'
        if health in NV:
            NVfam = NVfam + ' Health'
        if evil[0] in NV or evil[1] in NV:
            NVfam = NVfam + ' Evil'

        print('\nRegular:\n[Root: ' + root + '] Verb: ' + V)
        print('   NounI: ' + NI + ' | Fam:' + NIfam + '\n NounII: ' + NII + '  | Fam:' + NIIfam + '\n   NounIII: ' + NIII + ' | Fam:' + NIIIfam)
        print('NounIV: ' + NIV + ' | Fam:' + NIVfam + '\n   NounV: ' + NV + ' | Fam:' + NVfam)

        message = '[Root: ' + root + ']\nVerb: ' + V + '\n\nNounI: ' + NI + '\n |Fam:' + NIfam + '\nNounII: ' + NII + '\n |Fam:' + NIIfam + '\nNounIII: ' + NIII + '\n |Fam:' + NIIIfam + '\nNounIV: ' + NIV + '\n |Fam:' + NIVfam + '\nNounV: ' + NV + '\n |Fam:' + NVfam
        stomessage = '\n' + Verbs + '\n' + NounsI + '\n ' + NounsII + '\n   ' + NounsIII + '\n  ' + NounsIV + '\n   ' + NounsV

        mes = input('\nSto or Eng: ')
        if mes == 'Eng':
            w, h = font.getsize(message)
            x = 0
            y = 0
            draw.text((x, y), message, inky_display.RED, font)
            inky_display.set_image(img)
            inky_display.show()
        elif mes == 'Sto':
            w, h = font.getsize(stomessage)
            x = 80
            y = -67
            draw.text((x, y), stomessage, inky_display.RED, stofont)
            flipped = img.rotate(90)
            inky_display.set_image(flipped)
            inky_display.show()
