#MOD: Retrieves conjugations/declinations from dictionary and prints to inky

#tools for inky e-paper screen
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

#my MODs
import ModinkyStartupImage


#gets word as input returns it to program
def startup():
    word = input('Word: ')
    
    return word

#asks for tense if verb, then gets conjugation/declination, retunrs it to program as list
def GetDictionary(word, lines):
    #determines if verb or noun
    #if verb:
    if word.endswith('t') is True:
        tense = input('Tense?: ')
        if tense in ['present']:
            i = lines.index(word) + 4
            while True:
                if lines[i] == '* ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 4:i]
        elif tense in ['past']:
            i = lines.index(word) + 11
            while True:
                if lines[i] == '** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 11:i]
        elif tense in ['future']:
            i = lines.index(word) + 18
            while True:
                if lines[i] == '*** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 18:i]
        elif tense in ['Present Progressive']:
            i = lines.index(word) + 25
            while True:
                if lines[i] == '**** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 25:i]
        elif tense in ['Past Progressive']:
            i = lines.index(word) + 32
            while True:
                if lines[i] == '***** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 32:i]
        elif tense in ['Future Progressive']:
            i = lines.index(word) + 39
            while True:
                if lines[i] == '****** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 39:i]
    #If noun:
    else:
        i = lines.index(word) + 5
        while True:
            if lines[i] == '*******':
                break
            else:
                i += 1
        return lines[lines.index(word) + 5:i]

#the program called by the ChooseAProgram
def inkyPrintDictionary():
    #displays Conjugation startup screen on inky
    ModinkyStartupImage.StarUpPrintConDec()
    with open('/home/pi/Desktop/MyCode/LanguageProject/ConlangDatabase.txt', 'r') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]

    while True:
        word = startup()
        if word in ['Quit']:
            break
        else:
            text = '\n'.join(GetDictionary(word, lines))
            
            #boilerplate code for ink pHAT
            inky_display = InkyWHAT('red')
            inky_display.set_border(inky_display.WHITE)
            #screen dimension variable
            img = Image.new('P', (inky_display.WIDTH, inky_display.HEIGHT))
            draw = ImageDraw.Draw(img)
            
            #takes that str and sets proper variables
                #font select
            fontpath = '/home/pi/Desktop/MyCode/LanguageProject/Fonts/'
            if word.endswith('t') is True:
                font = ImageFont.truetype(fontpath + 'LinuxLibertinefattened/Linux-Libertine-fattened-Bold.ttf', 26)
                message = '\n\n' + text
            else:
                font = ImageFont.truetype(fontpath + 'LinuxLibertinefattened/Linux-Libertine-fattened-Bold.ttf', 18)
                message = text
            
            #grid variables: start in top left corner
            x = 0
            y = 0
            # uses variables to package str and send to screen
            draw.text((x, y), message, inky_display.RED, font)
            inky_display.set_image(img)
            inky_display.show()