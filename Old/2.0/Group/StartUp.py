#Startup Program
import WordConjugatorClass
import WordGeneratorClass
import ReadDictionaryTSelect as Dic

#Object Setup
Con = WordConjugatorClass.Conjugate()
Ran = WordGeneratorClass.RandomWordGenerator()

while True:
    program = input('Which Program?: ')
    if program in ['Conjugator']:
        Con.ConRecord()
    elif program in ['Word Generator']:
        Ran.RandomWord()
    elif program in ['Dictionary']:
        Dic.Dictionary()