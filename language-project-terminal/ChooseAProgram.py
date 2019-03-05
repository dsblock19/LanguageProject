#top level program: python3 /home/pi/Desktop/MyCode/LanguageProject/ChooseAProgram.py

import ModWordConjugator
import ModWordGenerator
#import ModReadDictionary
import ModReadDictionaryTSelect
#import inkyReadDictionary

while True:
    WordProgram = input('Which Program?: ')
    if  WordProgram in ['Conjugator']:
        ModWordConjugator.WordConjugator()
    elif WordProgram in ['Generator']:
        ModWordGenerator.WordGenerator()
    #elif WordProgram in ['Dictionary']:
        #ModReadDictionary.ReadDictionary()
    elif WordProgram in ['Dictionary']:
        ModReadDictionaryTSelect.ReadDictionary()
    #elif WordProgram in ['Dictionary']:
        #inkyReadDictionary.ReadDictionary()
    elif WordProgram in ['Quit']:
        break
    else:
        print('Error')
        print(' ')