#MOD: Gets input word and then classifies it, and conjugates/declines the word based on class

# tools
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

# conjugates if the word is a verb and asks tense to display
#present
def PresentVconjugate():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV 
    print('Conjugation:')
    print(' ')
    print('Present:')
    print(ProI + root + PrPI)
    print(ProII + root + PrPII)
    print(ProIII + root + PrPIII)
    print(ProIV + root + PrPIV)
    print(ProV + root + PrPV)
    print(' ')

#past
def PastVconjugate():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV 
    print('Conjugation:')
    print(' ')
    print('Past:')
    print(ProI + root + PaPI)
    print(ProII + root + PaPII)
    print(ProIII + root + PaPIII)
    print(ProIV + root + PaPIV)
    print(ProV + root + PaPV)
    print(' ')
    
#future
def FutureVconjugate():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV 
    print('Conjugation:')
    print(' ')
    print('Future:')
    print(ProI + root + FuPI)
    print(ProII + root + FuPII)
    print(ProIII + root + FuPIII)
    print(ProIV + root + FuPIV)
    print(ProV + root + FuPV)
    print(' ')

#Present Progressive
def PresentProVconjugate():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV 
    print('Conjugation:')
    print(' ')
    print('Present Progressive:')
    print(ProI + root + PrPgPI)
    print(ProII + root + PrPgPII)
    print(ProIII + root + PrPgPIII)
    print(ProIV + root + PrPgPIV)
    print(ProV + root + PrPgPV)
    print(' ')

#Past Progressive
def PastProVconjugate():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV 
    print('Conjugation:')
    print(' ')
    print('Past Progressive:')
    print(ProI + root + PaPgPI)
    print(ProII + root + PaPgPII)
    print(ProIII + root + PaPgPIII)
    print(ProIV + root + PaPgPIV)
    print(ProV + root + PaPgPV)
    print(' ')

#Future Progressive
def FutureProVconjugate():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV 
    print('Conjugation:')
    print(' ')
    print('Future Progressive:')
    print(ProI + root + FuPgPI)
    print(ProII + root + FuPgPII)
    print(ProIII + root + FuPgPIII)
    print(ProIV + root + FuPgPIV)
    print(ProV + root + FuPgPV)
    print(' ')

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
            PresentVconjugate()
        elif tense in ['past']:
            PastVconjugate()
        elif tense in ['future']:
            FutureVconjugate()
        elif tense in ['Present Progressive']:
            PresentProVconjugate()
        elif tense in ['Past Progressive']:
            PastProVconjugate()
        elif tense in ['Future Progressive']:
            FutureProVconjugate()
        else:
            print('error')
    elif Class in ['NounI', 'NounII', 'NounIII', 'NounIV', 'NounV', 'NounVI']:
        print('Conjugation?: No.')
        print('Not a Verb')


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
            print('Singular: ' + Sing + root)
            print('Dative: ' + random.choice(Vdative) + root)
            print('Acusative: ' + root + random.choice(acusative))
            print('Genitive: ' + root + genitive)
            print('Locative: ' + root + random.choice(locative))
            print(' ')
        elif word.startswith('i:i') is True:
            print('Singular: ' + Sing + root)
            print('Dative: ' + random.choice(Vdative) + root)
            print('Acusative: ' + root + random.choice(acusative))
            print('Genitive: ' + root + genitive)
            print('Locative: ' + root + random.choice(locative))
            print(' ')
        elif word.startswith(core_consonants) is True:
            print('Singular: ' + Sing + root)
            print('Dative: ' + random.choice(Cdative) + root)
            print('Acusative: ' + root + random.choice(acusative))
            print('Genitive: ' + root + genitive)
            print('Locative: ' + root + random.choice(locative))
            print(' ')
        elif word.startswith('i') is True:
            print('Singular: ' + Sing + root)
            print('Dative: ' + random.choice(Cdative) + root)
            print('Acusative: ' + root + random.choice(acusative))
            print('Genitive: ' + root + genitive)
            print('Locative: ' + root + random.choice(locative))
            print(' ')
    else:
        print('Not a Noun')
        print(' ')


# records conjugation/declination to .txt file
def logwords():
    global Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV 
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


def WordConjugator():
    global definition, word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative 
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV 
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII 
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII 
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV 
    word = input('Word: ')
    definition = input('Definition: ')
    classification()
    Class = classification()
    print('Class: ' + Class)
    Strip2Root()
    root = Strip2Root()
    print('Root: ' + root)
    ChooseTense()
    Ndecline()
    logwords()