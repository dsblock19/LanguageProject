#top level program: python3 /home/pi/Desktop/MyCode/LanguageProject/inky/inkyChooseAProgram.py &

from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

import ModinkyStartupImage
import ModinkyWordConjugator
import ModinkyWordGenerator
import ModinkyReadDictionary
import ModinkyPrintConDec

#boilerplate set up
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

# screen dimension variables
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

#set up font
fontpath = '/home/pi/Desktop/MyCode/Fonts/'
font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 18)


#set up startup message
startupmessage = '      istoth:\nLanguage in Stone\n \n \n      Which program?'
x = 0
y = 0

ModinkyStartupImage.StartupImage()

while True:
    draw.text((x, y), startupmessage, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()
    WordProgram = input('Which Program?: ')
    if  WordProgram in ['New Word']:
        ModinkyWordConjugator.NewWord()
    elif WordProgram in ['Generator']:
        ModinkyWordGenerator.WordGenerator()
    elif WordProgram in ['Dictionary']:
        ModinkyReadDictionary.ReadDictionary()
    elif WordProgram in ['Conjugator']:
        ModinkyPrintConDec.inkyPrintDictionary()
    elif WordProgram in ['Quit']:
        break
    else:
        print('Error')
        print(' ')
