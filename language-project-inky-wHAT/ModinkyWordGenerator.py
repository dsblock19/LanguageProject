#MOD: follows rules of the language to generate random root and accompanying family 

#tools
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
import buttonshim
import signal

import random
from time import sleep

#lists of all avalible sounds to the language
core_consonants = [ 'd', 't', 'c', 'k', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'x', 'th', 'st', 'v', 'j', 'ch', 'b', 'h', 'r' ]
core_vowels = [ 'aw', 'o', 'i', 'u', 'a', 'i:i', 'oo' ]
allsounds = core_consonants + core_vowels

#lists of possible endings avalible to the language
verb_ending = 't'
n_classI = [ 'i:i', 'aw', 'a' ]
n_classII = [ 'c', 'k', 'x' ]
n_classIII = [ 'st', 'th' ]
n_classIV = [ 'ms', 'm', 'i' ]
n_classV = [ 'o', 'e', 'ipa' ]
n_classVI = [ 'd', 'z', 'n', 'g', 'p', 'b' ]


#randomization to create roots out of the core CV (which is random)
def VCVCV():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    rt = random.choice(core_vowels) + core + random.choice(core_consonants) + random.choice(core_vowels)
    return rt
    
def CVCV():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    rt = core + random.choice(core_consonants) + random.choice(core_vowels)
    return rt 
 
def CVC():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    rt = core + random.choice(core_consonants)
    return rt   
    
def CV():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    rt = core
    return rt     



#turns the root (see above) into different types of nouns and verbs to create a simple family
def NounI():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    if root[-1] in ['o', 'i', 'u', 'oo']:
        NI = root + random.choice(core_consonants) + random.choice(n_classI)
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
        NI = root + random.choice(n_classI)
    return NI
    
def NounII():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    if root[-1] in ['d', 't', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'th', 'st', 'v', 'j', 'ch', 'b','h', 'r' ]:
        NII = root + random.choice(core_vowels) + random.choice(n_classII)
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
        NII = root + random.choice(n_classII)
    return NII
    
def NounIII():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    if root[-1] in ['c', 'k', 'x', 'd', 't', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r' ]:
        NIII = root + random.choice(core_vowels) + random.choice(n_classIII)
    elif root[-1] in ['st']:
        noST = ['th']
        NIII = root + random.choice(noST)
    elif root[-1] in ['th']:
        noTH = ['st']
        NIII = root + random.choice(noTH)
    else:
        NIII = root + random.choice(n_classIII)
    return NIII
    
def NounIV():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    if root[-1] in [ 'o', 'e', 'i', 'u', 'oo', 'i:i', 'aw', 'a']:
        noi = ['ms', 'm']
        NIV = root + random.choice(core_vowels)+ random.choice(noi)
    elif root[-1] in ['c', 'k', 'x', 'd', 't', 'z', 'n', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b', 'h', 'r' ]:
        NIV = root + random.choice(core_consonants) + 'i'
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
        NIV = root + random.choice(n_classIV)
    return NIV
    
def NounV():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    if root[-1] in [ 'i', 'u', 'oo', 'i:i', 'aw', 'a']:
        NV = root + random.choice(core_consonants) + random.choice(n_classV)
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
        NV = root + random.choice(n_classV)
    return NV

def NounVI():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    if root[-1] in ['st', 'th', 'c', 'k', 'x', 't', 's', 'm', 'sh', 'v', 'j', 'ch', 'h', 'r' ]:
        NVI = root + random.choice(core_vowels) + random.choice(n_classVI)
    elif root[-1] in ['d']:
        noD = ['z', 'n', 'g', 'p', 'b']
        NVI = root + random.choice(noD)
    elif root[-1] in ['z']:
        noZ = ['d', 'n', 'g', 'p', 'b']
        NVI = root + random.choice(noZ)
    elif root[-1] in ['n']:
        noN = ['d', 'z', 'g', 'p', 'b']
        NVI = root + random.choice(noN)
    elif root[-1] in ['g']:
        noG = ['d', 'z', 'n', 'p', 'b']
        NVI = root + random.choice(noG)
    elif root[-1] in ['p']:
        noP = ['d', 'z', 'g', 'n', 'b']
        NVI = root + random.choice(noP)
    elif root[-1] in ['b']:
        noB = ['d', 'z', 'g', 'p', 'n']
        NVI = root + random.choice(noB)
    else:
        NVI = root + random.choice(n_classVI)
    return NVI

def Verb():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    if root[-1] in ['t', 'st', 'th', 'c', 'k', 'x', 'd', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r']:
        V = root + random.choice(core_vowels) + verb_ending
    else:
        V = root + verb_ending
    return V


#logs the families on seperate lines in a .txt file
def logwords():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    f = open('/home/pi/Desktop/MyCode/LanguageProject/RandomFamily.txt', 'a')
    f.write('\n[Core: ' + core + ' | Root: ' + root + '] Verb: ' + Verbs + '\n')
    f.write('   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV + '\n NounVI: ' + NounsVI + '\n')
    f.close()


def WordGenerator():
    global core, core_vowels, core_consonants, root
    global Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI, verb_ending
    global n_classI, n_classII, n_classIII, n_classIV, n_classV, n_classVI
    while True:
        buttonshim.set_pixel(0xff, 0xff, 0x00)
        command = input('Command: ')
        if command in ['Quit']:
            break
        elif command in ['Go']:
            #makes core out of random selection of C + V
            core = random.choice(core_consonants) + random.choice(core_vowels)
            
            #picks a random addition to the core to make a root
            roots = [ CV(), VCVCV(), CVCV(), CVC() ]
            random_root = random.choice(roots)
            random_root
            root = random_root
            
            #takes the root and randomly adds endings to make a family
            Verbs = Verb()
            NounsI = NounI()
            NounsII = NounII()
            NounsIII = NounIII()
            NounsIV = NounIV()
            NounsV = NounV()
            NounsVI = NounVI()
            
            #message construction
            message = '[Core: ' + core + ' | Root: ' + root + '] Verb: ' + Verbs + '\n   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV + '\n NounVI: ' + NounsVI + '\n'
            
            #boilerplate code for ink pHAT
            inky_display = InkyWHAT('red')
            inky_display.set_border(inky_display.WHITE)
            #screen dimension variable
            img = Image.new('P', (inky_display.WIDTH, inky_display.HEIGHT))
            draw = ImageDraw.Draw(img)
            
            #takes that str and sets proper variables
                #font select
            fontpath = '/home/pi/Desktop/MyCode/LanguageProject/Fonts/'
            font = ImageFont.truetype(fontpath + 'LinuxLibertinefattened/Linux-Libertine-fattened-Bold.ttf', 16)
                #grid variables: start in top left corner
            x = 0
            y = 0
            # uses variables to package str and send to screen
                #
            draw.text((x, y), message, inky_display.RED, font)
            inky_display.set_image(img)
            inky_display.show()
            
            #logs family in .txt file
            logwords()
        else:
            print('error')
