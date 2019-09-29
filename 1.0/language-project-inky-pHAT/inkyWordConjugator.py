#toplevel: gets word, gets definition, strips word to root, conjugates/declines the word, and prints data to inky screen and logs in .txt file

# tools
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

import random

# avalible sounds in language
core_consonants = ( 'd', 't', 'k', 'z', 'n', 's', 'm', 'g', 'p', 'v', 'j', 'b', 'h', 'r' )
core_vowels = ( 'aw', 'o', 'u', 'a', 'oo', 'e' )
other_vowels = ( 'i:i', 'i' )
other_consonants = ( 'c', 'sh', 'th', 'st', 'ch', 'x' )
other_c = ( 'qua' )
all_vowels = core_vowels + other_vowels
all_consonants = core_consonants + other_consonants
allsounds = core_consonants + core_vowels + other_vowels + other_consonants

# endings to classify word as verb or noun and which class of verb/noun
RV = ('t')
NI = ( 'i:i', 'aw', 'a' )
NII = ( 'c', 'k', 'x' )
NIII = ( 'st', 'th' )
NIV = ( 'ms', 'm', 'i' )
NV = ( 'o', 'e', 'ipa' )
NVI = ( 'd', 'z', 'n', 'g', 'p', 'b' )

# pronoun groups
ProI = 'I/He/She/They(sing): '
ProII = 'You: '
ProIII = 'Yall/They(plural): '
ProIV = 'We(royal): '
ProV = 'We(exclusive): '

# verb endings
    #present
PrPI = 'taj'
PrPII = 'tast'
PrPIII = 'tasta'
PrPIV = 'tam'
PrPV = 'tama'
    #past
PaPI = 'ta'
PaPII = 'tas'
PaPIII = 'tasa'
PaPIV = 'tan'
PaPV = 'tana' 
    #future
FuPI = 'tua'
FuPII = 'tue'
FuPIII = 'tust' 
FuPIV = 'tun'
FuPV = 'tuna'
    #present progressive
PrPgPI = 'taja'
PrPgPII = 'tasta'
PrPgPIII = 'tast'
PrPgPIV = 'tama'
PrPgPV = 'tam'
    #past progressive
PaPgPI = 'tag'
PaPgPII = 'tasa'
PaPgPIII = 'tas'
PaPgPIV = 'tana'
PaPgPV = 'tan'
    #future progressive
FuPgPI = 'tui'
FuPgPII = 'tust'
FuPgPIII = 'tue'
FuPgPIV = 'tuna'
FuPgPV = 'tun'

# noun declination prefixes/suffixes
    #prefixes
#nominal number
Sing = 'ia'
Tri = 'io'
Pau = 'i'
#case
Vdative = ('m', 'n')
Cdative = ('ma', 'na')
instrumental = 'st'
comitative = 'u'
adesive = 'za'
allative = 'zi'
ablative = 'zo'
illative = 'thi'
inessive = 'tho'
    #suffixes
#case
acusative = ('m', 'ma', 'n', 'na')
genitive = 'a'
locative = ('ga', 'gua')


# compares word to endings to assign class to word
def classification():
    global RV, NI, NII, NIII, NIV, NV, NVI
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV    
    if word.endswith(RV) is True:
        Clas = 'RegularVerb'
    elif word.endswith(NI) is True:
        Clas = 'NounI'
    elif word.endswith(NII) is True:
        Clas = 'NounII'
    elif word.endswith(NIII) is True:
        Clas = 'NounIII'
    elif word.endswith(NIV) is True:
        Clas = 'NounIV'
    elif word.endswith(NV) is True:
        Clas = 'NounV'
    elif word.endswith(NVI) is True:
        Clas = 'NounVI'
    else:
        Clas = 'Not a Word'
    return Clas


# strips word of ending if verb or irregular noun
def Strip2Root():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV
    if Class in ['RegularVerb']:
        rt = word[:-1]
    elif Class in ['NounI', 'NounII', 'NounIII', 'NounIV', 'NounV', 'NounVI']:
        if word.endswith(core_vowels) is True:
            if word.startswith('i:i') is True:
                rt = word[2:]
            else:
                rt = word
        elif word.endswith('i:i') is True:
            if word.startswith('i:i') is True:
                rt = word[2:-2]
            else:
                rt = word[:-2]
        elif word.endswith(core_consonants) is True:
            if word.startswith('i:i') is True:
                rt = word[2:-1]
            else:
                rt = word[:-1]
        elif word.endswith('c') is True:
            if word.startswith('i:i') is True:
                rt = word[2:-1] + other_c
            else:
                rt = word[:-1] + other_c
        else:
            rt = word
    elif Class in ['Not a Word']:
        rt = '?'
    return rt


# declines if word is a noun
def Ndecline():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV
    print('Declination:')
    if Class in ['NounI', 'NounII', 'NounIII', 'NounIV', 'NounV', 'NounVI']:
        if word.startswith(core_vowels) is True:
            return 'Declination:\nSingular: ' + Sing + root + '\n' + 'Dative: ' + random.choice(Vdative) + root + '\n' + 'Acusative: ' + root + random.choice(acusative) + '\n' + 'Genitive: ' + root + genitive + '\n' + 'Locative: ' + root + random.choice(locative)
        elif word.startswith('i:i') is True:
            return 'Declination:\nSingular: ' + Sing + root + '\n' + 'Dative: ' + random.choice(Vdative) + root + '\n' + 'Acusative: ' + root + random.choice(acusative) + '\n' + 'Genitive: ' + root + genitive + '\n' + 'Locative: ' + root + random.choice(locative)
        elif word.startswith(core_consonants) is True:
            return 'Declination:\nSingular: ' + Sing + root + '\n' + 'Dative: ' + random.choice(Cdative) + root + '\n' + 'Acusative: ' + root + random.choice(acusative) + '\n' + 'Genitive: ' + root + genitive + '\n' + 'Locative: ' + root + random.choice(locative)
        elif word.startswith('i') is True:
            return 'Declination:\nSingular: ' + Sing + root + '\n' + 'Dative: ' + random.choice(Cdative) + root + '\n' + 'Acusative: ' + root + random.choice(acusative) + '\n' + 'Genitive: ' + root + genitive + '\n' + 'Locative: ' + root + random.choice(locative)
    else:
        return 'Declination: No'

def ChooseTense():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV
    if Class in ['RegularVerb']:
        tense = input('Tense: ')
        if tense in ['present']:
            return 'Present:' + '\n' + ProI + root + PrPI + '\n' + ProII + root + PrPII + '\n' + ProIII + root + PrPIII + '\n' + ProIV + root + PrPIV + '\n' + ProV + root + PrPV
        elif tense in ['past']:
            return 'Past:' + '\n' + ProI + root + PaPI + '\n' + ProII + root + PaPII + '\n' + ProIII + root + PaPIII + '\n' + ProIV + root + PaPIV + '\n' + ProV + root + PaPV
        elif tense in ['future']:
            return 'Future:' + '\n' + ProI + root + FuPI + '\n' + ProII + root + FuPII + '\n' + ProIII + root + FuPIII + '\n' + ProIV + root + FuPIV + '\n' + ProV + root + FuPV
        elif tense in ['Present Progressive']:
            return 'Present Progressive:' + '\n' + ProI + root + PrPgPI + '\n' + ProII + root + PrPgPII + '\n' + ProIII + root + PrPgPIII + '\n' + ProIV + root + PrPgPIV + '\n' + ProV + root + PrPgPV
        elif tense in ['Past Progressive']:
            return 'Past Progressive:' + '\n' + ProI + root + PaPgPI + '\n' + ProII + root + PaPgPII + '\n' + ProIII + root + PaPgPIII + '\n' + ProIV + root + PaPgPIV + '\n' + ProV + root + PaPgPV
        elif tense in ['Future Progressive']:
            return 'Future Progressive:' + '\n' + ProI + root + FuPgPI + '\n' + ProII + root + FuPgPII + '\n' + ProIII + root + FuPgPIII + '\n' + ProIV + root + FuPgPIV + '\n' + ProV + root + FuPgPV
        else:
            return 'error'
    elif Class in ['NounI', 'NounII', 'NounIII', 'NounIV', 'NounV', 'NounVI']:
        return 'Conjugation: No'


while True:
    word = input('Word: ')
    if word in ['Quit']:
        break
    else:
        definition = input('Definition: ')
        Class = classification()
        root = Strip2Root()
        declination = Ndecline()
        conjugation = ChooseTense()
        
        
        #log information to .txt
        f = open('/home/pi/Desktop/ConlangDatabase.txt', 'a')
        f.write('\n \n' + word + '\n')
        f.write('Definition: ' + definition + '\n')
        f.write('Class: ' + Class + '\n')
        if Class in ['RegularVerb']:
            f.write('Conjugation?: Yes \n')
            # present
            f.write('Present: \n  ')
            f.write(ProI + root + PrPI + ' \n  ' + ProII + root + PrPII + ' \n  ')
            f.write(ProIII + root + PrPIII + ' \n')
            f.write('  ' + ProIV + root + PrPIV + ' \n  ' + ProV + root + PrPV + ' \n')
            f.write('*' + ' \n')
            # past
            f.write('Past: \n  ')
            f.write(ProI + root + PaPI + ' \n  ' + ProII + root + PaPII + ' \n  ')
            f.write(ProIII + root + PaPIII + ' \n')
            f.write('  ' + ProIV + root + PaPIV + ' \n  ' + ProV + root + PaPV + ' \n')
            f.write('**' + ' \n')
            # future
            f.write('Future: \n  ')
            f.write(ProI + root + FuPI + ' \n  ' + ProII + root + FuPII + ' \n  ')
            f.write(ProIII + root + FuPIII + ' \n')
            f.write('  ' + ProIV + root + FuPIV + ' \n  ' + ProV + root + FuPV + ' \n')
            f.write('***' + ' \n')
            # present progressive
            f.write('Present Progressive: \n  ')
            f.write(ProI + root + PrPgPI + ' \n  ' + ProII + root + PrPgPII + ' \n  ')
            f.write(ProIII + root + PrPgPIII + ' \n')
            f.write('  ' + ProIV + root + PrPgPIV + ' \n  ' + ProV + root + PrPgPV + ' \n')
            f.write('****' + ' \n')
            # past progressive
            f.write('Past Progressive: \n  ')
            f.write(ProI + root + PaPgPI + ' \n  ' + ProII + root + PaPgPII + ' \n  ')
            f.write(ProIII + root + PaPgPIII + ' \n')
            f.write('  ' + ProIV + root + PaPgPIV + ' \n  ' + ProV + root + PaPgPV + ' \n')
            f.write('*****' + ' \n')
            # future progressive
            f.write('Future Progressive: \n  ')
            f.write(ProI + root + FuPgPI + ' \n  ' + ProII + root + FuPgPII + ' \n  ')
            f.write(ProIII + root + FuPgPIII + ' \n')
            f.write('  ' + ProIV + root + FuPgPI + ' \n  ' + ProV + root + FuPgPV + ' \n')
            f.write('******' + ' \n')
            # noun
            f.write( 'Declination?: No' + '\n' + '  Not a Noun' + '\n')
            # end mark
            f.write('*******' + '\n')
            # close
            f.close()
        elif Class in ['NounI', 'NounII', 'NounIII', 'NounIV', 'NounV', 'NounVI']:
            if word.startswith(core_vowels) is True:
                f.write('Conjugation?: No \n' + '   Not a Verb \n')
                f.write('Declination?: Yes \n')
                #nominal number suffixes
                f.write('   Singular: ' + Sing + root + '\n')
                f.write('   Trial: ' + Tri + root + '\n')
                f.write('   Paucal:' + Pau + root + '\n')
                #case suffixes
                f.write('   Dative: ' + random.choice(Vdative) + root + '\n')
                #case suffixes II
                f.write('   Instrumental: ' + instrumental + root + '\n')
                f.write('   Comitative: ' + comitative + root + '\n')
                f.write('   Adesive: ' + adesive + root + '\n')
                f.write('   Allative: ' + allative + root + '\n')
                f.write('   Ablative: ' + ablative + root + '\n')
                f.write('   Illative: ' + illative + root + '\n')
                f.write('   Inessive: ' + inessive + root + '\n')
                #case prefixes
                f.write('   Acusative: ' + root + random.choice(acusative) + '\n')
                f.write('   Genitive: ' + root + genitive + '\n')
                #case prefixes II
                f.write('   Locative: ' + root + random.choice(locative) + '\n')
                # end mark
                f.write('*******' + '\n')
                f.close()
            elif word.startswith(core_consonants) is True:
                f.write('Conjugation?: No \n' + '   Not a Verb \n')
                f.write('Declination?: Yes \n')
                f.write('   Singular: ' + Sing + root + '\n')
                f.write('   Trial: ' + Tri + root + '\n')
                f.write('   Paucal:' + Pau + root + '\n')
                f.write('   Dative: ' + random.choice(Cdative) + root + '\n')
                f.write('   Instrumental: ' + instrumental + root + '\n')
                f.write('   Comitative: ' + comitative + root + '\n')
                f.write('   Adesive: ' + adesive + root + '\n')
                f.write('   Allative: ' + allative + root + '\n')
                f.write('   Ablative: ' + ablative + root + '\n')
                f.write('   Illative: ' + illative + root + '\n')
                f.write('   Inessive: ' + inessive + root + '\n')
                f.write('   Acusative: ' + root + random.choice(acusative) + '\n')
                f.write('   Genitive: ' + root + genitive + '\n')
                f.write('   Locative: ' + root + random.choice(locative) + '\n')
                # end mark
                f.write('*******' + '\n')
                f.close()
            elif word.startswith(other_vowels) is True:
                f.write('Conjugation?: No \n' + '   Not a Verb \n')
                f.write('Declination?: Yes \n')
                #nominal number suffixes
                f.write('   Singular: ' + Sing + root + '\n')
                f.write('   Trial: ' + Tri + root + '\n')
                f.write('   Paucal:' + Pau + root + '\n')
                #case suffixes
                f.write('   Dative: ' + random.choice(Vdative) + root + '\n')
                #case suffixes II
                f.write('   Instrumental: ' + instrumental + root + '\n')
                f.write('   Comitative: ' + comitative + root + '\n')
                f.write('   Adesive: ' + adesive + root + '\n')
                f.write('   Allative: ' + allative + root + '\n')
                f.write('   Ablative: ' + ablative + root + '\n')
                f.write('   Illative: ' + illative + root + '\n')
                f.write('   Inessive: ' + inessive + root + '\n')
                #case prefixes
                f.write('   Acusative: ' + root + random.choice(acusative) + '\n')
                f.write('   Genitive: ' + root + genitive + '\n')
                #case prefixes II
                f.write('   Locative: ' + root + random.choice(locative) + '\n')
                # end mark
                f.write('*******' + '\n')
                f.close()
        
        
        #boilerplate code for ink pHAT
        inky_display = InkyPHAT("red")
        inky_display.set_border(inky_display.WHITE)
        
        #screen dimension variable
        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)
        
        fontpath = '/home/pi/Desktop/MyCode/Fonts/'
        font = ImageFont.truetype(fontpath + 'LinuxLibertinefattened/Linux-Libertine-fattened-Bold.ttf', 15)
        #message construction
        if Class in ['NounI', 'NounII', 'NounIII', 'NounIV', 'NounV', 'NounVI']: 
            message = word + '\nDefinition: ' + definition + '\n' + declination
        else:
            message = word + '\n Definition: ' + definition + '\n' + conjugation
        #grid variables: start in top left corner
        x = 0
        y = 0
        
        # uses variables to package str and send to screen
        draw.text((x, y), message, inky_display.RED, font)
        inky_display.set_image(img)
        inky_display.show()