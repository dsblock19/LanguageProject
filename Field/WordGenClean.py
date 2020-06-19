#LIBRARIES
import random


#FUNCTIONS
#Word Building w/in Class
def NnI(WClass, root):
    if root[-1] in ['o', 'i', 'u', 'oo']:
        NI = root + random.choice(core_consonants) + random.choice(WClass[1])
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
    return NI

def NnII(WClass, root):
    if root[-1] in ['d', 't', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'th', 'st', 'v', 'j', 'ch', 'b','h', 'r' ]:
        NII = root + random.choice(core_vowels) + random.choice(WClass[2])
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
    return NII

def NnIII(WClass, root):
    if root[-1] in ['c', 'k', 'x', 'd', 't', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r' ]:
        NIII = root + random.choice(core_vowels) + random.choice(WClass[3])
    elif root[-1] in ['st']:
        noST = ['th']
        NIII = root + random.choice(noST)
    elif root[-1] in ['th']:
        noTH = ['st']
        NIII = root + random.choice(noTH)
    else:
        NIII = root + random.choice(WClass[3])
    return NIII

def NnIV(allcategories, WClass, root):
    if root[-1] in [ 'o', 'e', 'i', 'u', 'oo', 'i:i', 'aw', 'a']:
        noi = ['ms', 'm']
        NIV = root + random.choice(core_vowels)+ random.choice(noi)
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
    return NIV

def NnV(WClass, root):
    if root[-1] in [ 'i', 'u', 'oo', 'i:i', 'aw', 'a']:
        NV = root + random.choice(core_consonants) + random.choice(WClass[5])
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
    return NV

def Ve(allcategories, WClass, root):
    if root[-1] in ['t', 'st', 'th', 'c', 'k', 'x', 'd', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r']:
        V = root + random.choice(allcategories[1]) + WClass[0]
    else:
        V = root + WClass[0]
    return V

#Build New Family
def NewFam(NnI, NnII, NnIII, NnIV, NnV, Ve):
    #SETUP
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
    if family == 'Holy':
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

    #Class
    NI = NnI(WClass, root)
    NII = NnII(WClass, root)
    NIII = NnIII(WClass, root)
    NIV = NnIV(allcategories, WClass, root)
    NV = NnV(WClass, root)
    V = Ve(allcategories, WClass, root)

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
    f = open('/home/pi/Desktop/MyCode/LanguageProject/Output/RandomFamily.txt', 'a')
    f.write('\n\n[Root: ' + root + '] Verb: ' + V + '\n')
    f.write('   NounI: ' + NI + '\n NounII: ' + NII + '\n   NounIII: ' + NIII + '\n NounIV: ' + NIV + '\n   NounV: ' + NV)
    f.close()
    stof = open('/home/pi/Desktop/MyCode/LanguageProject/Output/StoIthRandomFamily.txt', 'a')
    stof.write('\n\n[Root: ' + root + '] Verb: ' + Verbs + '\n')
    stof.write('   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV)
    stof.close()

    #Print Results
    print('\nIn Sto:\n[Root: ' + root + '] Verb: ' + Verbs)
    print('   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV)
    #NIfam
    NIfam = ''
    if NI.find(holy[0]) != -1 or NI.find(holy[1] != -1):
        NIfam = NIfam + ' Holy'
    if NI.find(building[0]) != -1 or NI.find(building[1]) != -1:
        NIfam = NIfam + ' Building'
    if NI.find(domanimal[0]) != -1 or NI.find(domanimal[1]) != -1 or NI.find(domanimal[2]) != -1:
        NIfam = NIfam + ' Domestic Animal'
    if NI.find(stone[0]) != -1 or NI.find(stone[1]) != -1:
        NIfam = NIfam + ' Stone'
    if NI.find(forest[0]) != -1 or NI.find(forest[1]) != -1:
        NIfam = NIfam + ' Forest'
    if NI.find(water) != -1:
        NIfam = NIfam + ' Water'
    if NI.find(atoms[0]) != -1 or NI.find(atoms[1]) != -1:
        NIfam = NIfam + ' Atoms'
    if NI.find(thebody[0]) != -1 or NI.find(thebody[1]) != -1 or NI.find(thebody[2]) != -1:
        NIfam = NIfam + ' The Body'
    if NI.find(writing) != -1:
        NIfam = NIfam + ' Writing'
    if NI.find(human) != -1:
        NIfam = NIfam + ' Human'
    if NI.find(health) != -1:
        NIfam = NIfam + ' Health'
    if NI.find(evil[0]) != -1 or NI.find(evil[1]) != -1:
        NIfam = NIfam + ' Evil'
    #NIIfam
    NIIfam = ''
    if NII in Rfam[0]:
        NIIfam = NIIfam + ' Holy'
    if NII in Rfam[1]:
        NIIfam = NIIfam + ' Building'
    if NII in Rfam[2]:
        NIIfam = NIIfam + ' Domestic Animal'
    if NII in Rfam[3]:
        NIIfam = NIIfam + ' Stone'
    if NII in Rfam[4]:
        NIIfam = NIIfam + ' Forest'
    if NII in Rfam[5]:
        NIIfam = NIIfam + ' Water'
    if NII in Rfam[6]:
        NIIfam = NIIfam + ' Atoms'
    if NII in Rfam[7]:
        NIIfam = NIIfam + ' The Body'
    if NII in Rfam[8]:
        NIIfam = NIIfam + ' Writing'
    if NII in Rfam[9]:
        NIIfam = NIIfam + ' Human'
    if NII in Rfam[10]:
        NIIfam = NIIfam + ' Health'
    if NII in Rfam[11]:
        NIIfam = NIIfam + ' Evil'
    #NIIIfam
    NIIIfam = ''
    if NIII in Rfam[0]:
        NIIIfam = NIIIfam + ' Holy'
    if NIII in Rfam[1]:
        NIIIfam = NIIIfam + ' Building'
    if NIII in Rfam[2]:
        NIIIfam = NIIIfam + ' Domestic Animal'
    if NIII in Rfam[3]:
        NIIIfam = NIIIfam + ' Stone'
    if NIII in Rfam[4]:
        NIIIfam = NIIIfam + ' Forest'
    if NIII in Rfam[5]:
        NIIIfam = NIIIfam + ' Water'
    if NIII in Rfam[6]:
        NIIIfam = NIIIfam + ' Atoms'
    if NIII in Rfam[7]:
        NIIIfam = NIIIfam + ' The Body'
    if NIII in Rfam[8]:
        NIIIfam = NIIIfam + ' Writing'
    if NIII in Rfam[9]:
        NIIIfam = NIIIfam + ' Human'
    if NIII in Rfam[10]:
        NIIIfam = NIIIfam + ' Health'
    if NIII in Rfam[11]:
        NIIIfam = NIIIfam + ' Evil'
    #NIVfam
    NIVfam = ''
    if NIV in Rfam[0]:
        NIVfam = NIVfam + ' Holy'
    if NIV in Rfam[1]:
        NIVfam = NIVfam + ' Building'
    if NIV in Rfam[2]:
        NIVfam = NIVfam + ' Domestic Animal'
    if NIV in Rfam[3]:
        NIVfam = NIVfam + ' Stone'
    if NIV in Rfam[4]:
        NIVfam = NIVfam + ' Forest'
    if NIV in Rfam[5]:
        NIVfam = NIVfam + ' Water'
    if NIV in Rfam[6]:
        NIVfam = NIVfam + ' Atoms'
    if NIV in Rfam[7]:
        NIVfam = NIVfam + ' The Body'
    if NIV in Rfam[8]:
        NIVfam = NIVfam + ' Writing'
    if NIV in Rfam[9]:
        NIVfam = NIVfam + ' Human'
    if NIV in Rfam[10]:
        NIVfam = NIVfam + ' Health'
    if NIV in Rfam[11]:
        NIVfam = NIVfam + ' Evil'
    #NVfam
    NVfam = ''
    if NV in Rfam[0]:
        NVfam = NVfam + ' Holy'
    if NV in Rfam[1]:
        NVfam = NVfam + ' Building'
    if NV in Rfam[2]:
        NVfam = NVfam + ' Domestic Animal'
    if NV in Rfam[3]:
        NVfam = NVfam + ' Stone'
    if NV in Rfam[4]:
        NVfam = NVfam + ' Forest'
    if NV in Rfam[5]:
        NVfam = NVfam + ' Water'
    if NV in Rfam[6]:
        NVfam = NVfam + ' Atoms'
    if NV in Rfam[7]:
        NVfam = NVfam + ' The Body'
    if NV in Rfam[8]:
        NVfam = NVfam + ' Writing'
    if NV in Rfam[9]:
        NVfam = NVfam + ' Human'
    if NV in Rfam[10]:
        NVfam = NVfam + ' Health'
    if NV in Rfam[11]:
        NVfam = NVfam + ' Evil'

    print('\nRegular:\n[Root: ' + root + '] Verb: ' + V)
    print('   NounI: ' + NI + ' | Fam:' + NIfam + '\n NounII: ' + NII + '  | Fam:' + NIIfam + '\n   NounIII: ' + NIII + ' | Fam:' + NIIIfam)
    print('NounIV: ' + NIV + ' | Fam:' + NIVfam + '\n   NounV: ' + NV + ' | Fam:' + NVfam)

#Loop
while True:
    NewFam(NnI, NnII, NnIII, NnIV, NnV, Ve)
