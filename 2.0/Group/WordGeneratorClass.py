#toplevel: follows rules of the language to generate random root and accompanying family

#tools
import random

class RandomWordGenerator:
    #Vars
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

    #Functions
    #randomization to create roots out of the core CV (which is random)
    def VCVCV(core):
        rt = random.choice(core_vowels) + core + random.choice(core_consonants) + random.choice(core_vowels)
        return rt

    def CVCV(core):
        rt = core + random.choice(core_consonants) + random.choice(core_vowels)
        return rt

    def CVC(core):
        rt = core + random.choice(core_consonants)
        return rt

    def CV(core):
        rt = core
        return rt

    #turns the root (see above) into different types of nouns and verbs to create a simple family
    def NounI(core, root):
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

    def NounII(core, root):
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

    def NounIII(core, root):
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

    def NounIV(core, root):
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

    def NounV(core, root):
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

    def NounVI(core, root):
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

    def Verb(core, root):
        if root[-1] in ['t', 'st', 'th', 'c', 'k', 'x', 'd', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'v', 'j', 'ch', 'b','h', 'r']:
            V = root + random.choice(core_vowels) + verb_ending
        else:
            V = root + verb_ending
        return V

    #converts characters for Sto-Ith
    def StoCon(core, root, Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI):
        #Make Upper Case
        core = core.upper()
        root = root.upper()
        Verbs = Verbs.upper()
        NounsI = NounsI.upper()
        NounsII = NounsII.upper()
        NounsIII = NounsIII.upper()
        NounsIV = NounsIV.upper()
        NounsV = NounsV.upper()
        NounsVI = NounsVI.upper()
        #Font Specific Change
        #ST --> F
        core = core.replace('ST', 'F')
        root = root.replace('ST', 'F')
        Verbs = Verbs.replace('ST', 'F')
        NounsI = NounsI.replace('ST', 'F')
        NounsII = NounsII.replace('ST', 'F')
        NounsIII = NounsIII.replace('ST', 'F')
        NounsIV = NounsIV.replace('ST', 'F')
        NounsV = NounsV.replace('ST', 'F')
        NounsVI = NounsVI.replace('ST', 'F')
        #OO --> L
        core.replace('OO', 'L')
        core = root.replace('OO', 'L')
        Verbs = Verbs.replace('OO', 'L')
        NounsI = NounsI.replace('OO', 'L')
        NounsII = NounsII.replace('OO', 'L')
        NounsIII = NounsIII.replace('OO', 'L')
        NounsIV = NounsIV.replace('OO', 'L')
        NounsV = NounsV.replace('OO', 'L')
        NounsVI = NounsVI.replace('OO', 'L')
        #SH --> Q
        core = core.replace('SH', 'Q')
        root = root.replace('SH', 'Q')
        Verbs = Verbs.replace('SH', 'Q')
        NounsI = NounsI.replace('SH', 'Q')
        NounsII = NounsII.replace('SH', 'Q')
        NounsIII = NounsIII.replace('SH', 'Q')
        NounsIV = NounsIV.replace('SH', 'Q')
        NounsV = NounsV.replace('SH', 'Q')
        NounsVI = NounsVI.replace('SH', 'Q')
        #AW --> W
        core = core.replace('AW', 'W')
        root = root.replace('AW', 'W')
        Verbs = Verbs.replace('AW', 'W')
        NounsI = NounsI.replace('AW', 'W')
        NounsII = NounsII.replace('AW', 'W')
        NounsIII = NounsIII.replace('AW', 'W')
        NounsIV = NounsIV.replace('AW', 'W')
        NounsV = NounsV.replace('AW', 'W')
        NounsVI = NounsVI.replace('AW', 'W')
        #I:I --> Y
        core = core.replace('I:I', 'Y')
        root = root.replace('I:I', 'Y')
        Verbs = Verbs.replace('I:I', 'Y')
        NounsI = NounsI.replace('I:I', 'Y')
        NounsII = NounsII.replace('I:I', 'Y')
        NounsIII = NounsIII.replace('I:I', 'Y')
        NounsIV = NounsIV.replace('I:I', 'Y')
        NounsV = NounsV.replace('I:I', 'Y')
        NounsVI = NounsVI.replace('I:I', 'Y')
        #CH --> @
        core = core.replace('CH', '@')
        root = root.replace('CH', '@')
        Verbs = Verbs.replace('CH', '@')
        NounsI = NounsI.replace('CH', '@')
        NounsII = NounsII.replace('CH', '@')
        NounsIII = NounsIII.replace('CH', '@')
        NounsIV = NounsIV.replace('CH', '@')
        NounsV = NounsV.replace('CH', '@')
        NounsVI = NounsVI.replace('CH', '@')
        #TH --> #
        core = core.replace('TH', '#')
        root = root.replace('TH', '#')
        Verbs = Verbs.replace('TH', '#')
        NounsI = NounsI.replace('TH', '#')
        NounsII = NounsII.replace('TH', '#')
        NounsIII = NounsIII.replace('TH', '#')
        NounsIV = NounsIV.replace('TH', '#')
        NounsV = NounsV.replace('TH', '#')
        NounsVI = NounsVI.replace('TH', '#')
        print('\n' + core + ' ' + root + ' ' + Verbs + ' ' + NounsI + ' ' + NounsII + ' ' + NounsIII + ' ' + NounsIV + ' ' + NounsV + ' ' + NounsVI + '\n')
        return core, root, Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI

    #logs the families on seperate lines in a .txt file
    def logwords(core, root, Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI):
        f = open('/home/pi/Desktop/MyCode/LanguageProject/Output/RandomFamily.txt', 'a')
        f.write('\n\n[Core: ' + core + ' | Root: ' + root + '] Verb: ' + Verbs + '\n')
        f.write('   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV + '\n NounVI: ' + NounsVI)
        f.close()
        stof = open('/home/pi/Desktop/MyCode/LanguageProject/Output/StoIthRandomFamily.txt', 'a')
        stof.write('\n\n[Core: ' + Stocore + ' | Root: ' + Storoot + '] Verb: ' + StoVerbs + '\n')
        stof.write('NounI: ' + StoNounsI + '\nNounII: ' + StoNounsII + '\nNounIII: ' + StoNounsIII + '\nNounIV: ' + StoNounsIV + '\nNounV: ' + StoNounsV + '\nNounVI: ' + StoNounsVI)
        stof.close()


    def RandomWord(self):
        command = input('Command: ')
        if command in ['Quit']:
            pass
        elif command in ['Go']:
            #makes core out of random selection of C + V
            core = random.choice(RandomWordGenerator.core_consonants) + random.choice(RandomWordGenerator.core_vowels)

            #picks a random addition to the core to make a root
            roots = [ RandomWordGenerator.CV(core), RandomWordGenerator.VCVCV(core), RandomWordGenerator.CVCV(core), RandomWordGenerator.CVC(core) ]
            random_root = random.choice(roots)
            root = random_root

            #takes the root and randomly adds endings to make a family
            Verbs = RandomWordGenerator.Verb(core, root)
            NounsI = RandomWordGenerator.NounI(core, root)
            NounsII = RandomWordGenerator.NounII(core, root)
            NounsIII = RandomWordGenerator.NounIII(core, root)
            NounsIV = RandomWordGenerator.NounIV(core, root)
            NounsV = RandomWordGenerator.NounV(core, root)
            NounsVI = RandomWordGenerator.NounVI(core, root)

            #message construction
            message = '[Core: ' + core + ' | Root: ' + root + '] Verb: ' + Verbs + '\n   NounI: ' + NounsI + '\n NounII: ' + NounsII + '\n   NounIII: ' + NounsIII + '\n NounIV: ' + NounsIV + '\n   NounV: ' + NounsV + '\n NounVI: ' + NounsVI + '\n'

            #Print Results
            print(message)
            #Convert for Sto-Ith Font
            Stocore, Storoot, StoVerbs, StoNounsI, StoNounsII, StoNounsIII, StoNounsIV, StoNounsV, StoNounsVI = RandomWordGenerator.StoCon(core, root, Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI)
            stomessage = 'For StoIth (Sto Font):\n\n[Core: ' + Stocore + ' | Root: ' + Storoot + '] Verb: ' + StoVerbs + '\n   NounI: ' + StoNounsI + '\n NounII: ' + StoNounsII + '\n   NounIII: ' + StoNounsIII + '\n NounIV: ' + StoNounsIV + '\n   NounV: ' + StoNounsV + '\n NounVI: ' + StoNounsVI + '\n'

            print(stomessage)

            #log words
            RandomWordGenerator.logwords(core, root, Verbs, NounsI, NounsII, NounsIII, NounsIV, NounsV, NounsVI)

        else:
            print('error')
