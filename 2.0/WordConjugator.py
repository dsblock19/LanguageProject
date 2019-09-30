#toplevel: gets word, gets definition, strips word to root, conjugates/declines the word, and prints data to terminal and logs in .txt file

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

# VERB ENDINGS
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

# NOUN DECLINATION
#PREFIXES
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
#SUFFIXES
#case
acusative = ('m', 'ma', 'n', 'na')
genitive = 'a'
locative = ('ga', 'gua')


# compares word to endings to assign class to word
def classification(word, RV, NI, NII, NIII, NIV, NV, NVI):
    if word.endswith(RV) is True:
        if word.endswith(NIII) is True:
            Clas = 'NounIII'
        else:
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
def Strip2Root(word, Class, core_vowels, core_consonants, other_vowels, other_consonants, other_c):
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
    global word, Class, root
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative
    global illative, inessive, acusative, genitive, locative
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

# allows choosing tense to print if verb
def ChooseTense():
    global Class, root
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

# converts word to sto-ith font and writes in .txt
def StoWord(word, definition, Class):
    #Make Upper Case
    stoword = word.upper()
    #Font Specific Change
    #ST --> F
    stoword = stoword.replace('ST', 'F')
    #OO --> L
    stoword = stoword.replace('OO', 'L')
    #SH --> Q
    stoword = stoword.replace('SH', 'Q')
    #AW --> W
    stoword = stoword.replace('AW', 'W')
    #I:I --> Y
    stoword = stoword.replace('I:I', 'Y')
    #CH --> @
    stoword = stoword.replace('CH', '@')
    #TH --> #
    stoword = stoword.replace('TH', '#')
    stof = open('/home/pi/Desktop/MyCode/LanguageProject/Output/StoIthFont.txt', 'a')
    stof.write('\n \n' + word + ' = ' + stoword + '\n')
    stof.write('Definition: ' + definition + '\n')
    stof.write('Class: ' + Class + '; ')
    if Class in ['NounI']:
        stof.write('Humans & Their Things'+ '\n')
    elif Class in ['NounII']:
        stof.write('Animate Objects & Nature'+ '\n')
    elif Class in ['NounIII']:
        stof.write('Inanimate Objects of Higher Value'+ '\n')
    elif Class in ['NounIV']:
        stof.write('Inanimate Objects of Lower Value'+ '\n')
    elif Class in ['NounV']:
        stof.write('Intangibles, Ideas, Concepts, & Teaching'+ '\n')
    elif Class in ['NounVI']:
        stof.write('Everything Else'+ '\n')
    elif Class in ['RegularVerb']:
        stof.write('Verb'+ '\n')
    stof.close()
    return word + ' = ' + stoword

# logs word in database .txt
def LogDataBase():
    global word, Class, root, core_vowels, core_consonants, other_vowels, other_consonants, other_c
    global Sing, Tri, Pau, Vdative, Cdative, instrumental, comitative, adesive, allative, ablative
    global illative, inessive, acusative, genitive, locative
    global PrPI, PrPII, PrPIII, PrPIV, PrPV, PaPI, PaPII, PaPIII, PaPIV
    global PaPV, FuPI, FuPII, FuPIII, FuPIV, FuPV, PrPgPI, PrPgPII
    global PrPgPIII, PrPgPIV, PrPgPV, PaPgPI, PaPgPII, PaPgPIII
    global PaPgPIV, PaPgPV, FuPgPI, FuPgPII, FuPgPIII, FuPgPIV, FuPgPV
    #log information to .txt
    f = open('/home/pi/Desktop/MyCode/LanguageProject/Output/ConlangDatabase.txt', 'a')
    f.write('\n \n' + word + '\n')
    f.write('Definition: ' + definition + '\n')
    f.write('Class: ' + Class + '; ')
    if Class in ['NounI']:
        f.write('Humans & Their Things'+ '\n')
    elif Class in ['NounII']:
        f.write('Animate Objects & Nature'+ '\n')
    elif Class in ['NounIII']:
        f.write('Inanimate Objects of Higher Value'+ '\n')
    elif Class in ['NounIV']:
        f.write('Inanimate Objects of Lower Value'+ '\n')
    elif Class in ['NounV']:
        f.write('Intangibles, Ideas, Concepts, & Teaching'+ '\n')
    elif Class in ['NounVI']:
        f.write('Everything Else'+ '\n')
    elif Class in ['RegularVerb']:
        f.write('Verb'+ '\n')
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


while True:
    word = input('Word: ')
    if word in ['Quit']:
        break
    else:
        definition = input('Definition: ')
        Class = classification(word, RV, NI, NII, NIII, NIV, NV, NVI)
        root = Strip2Root(word, Class, core_vowels, core_consonants, other_vowels, other_consonants, other_c)
        declination = Ndecline()
        conjugation = ChooseTense()
        LogDataBase()
        stoword = StoWord(word, definition, Class)
        print('\nWord: ' + word)
        print('Definition: ' + definition)
        print(declination)
        print('Conjugation: ' + conjugation)
        print('\nStoWord: ' + stoword + '\n')