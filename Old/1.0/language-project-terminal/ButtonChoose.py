#top level program: python3 /home/pi/Desktop/MyCode/LanguageProject/ButtonChoose.py

from gpiozero import Button
from time import sleep

import ModWordConjugator
import ModWordGenerator
#import ModReadDictionary
import ModReadDictionaryTSelect
#import inkyReadDictionary

dictionary = Button(2)
conjugator = Button(3)
wordgenerator = Button(17)
breaking = Button(27)

while True:
    if  conjugator.is_pressed:
        ModWordConjugator.WordConjugator()
        sleep(1)
    elif wordgenerator.is_pressed:
        ModWordGenerator.WordGenerator()
        sleep(1)
    #elif dictionary.is_pressed:
        #ModReadDictionary.ReadDictionary()
        #sleep(1)
    elif dictionary.is_pressed:
        ModReadDictionaryTSelect.ReadDictionary()
        sleep(1)
    #elif dictionary.is_pressed:
        #inkyReadDictionary.ReadDictionary()
        #sleep(1)
    elif breaking.is_pressed:
        break