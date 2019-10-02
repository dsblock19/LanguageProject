#Startup Program
import WordConjugatorClass
import WordGeneratorClass
import ReadDictionaryTSelect

#Object Setup
Con = WordConjugatorClass()
Ran = WordGeneratorClass()
Dic = ReadDictionaryTSelect()

while True:
    program = input('Which Program?: ')
    if program in ['Conjugator']:
        Con.ConRecord()
    elif program in ['Word Generator']:
        Ran.RandomWord()
    elif program in ['Dictionary']:
        Dic.Dictionary()
