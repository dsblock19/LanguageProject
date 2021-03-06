#MOD: takes input and reads entry based on input for inky pHAT

#tools for inky e-paper screen
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

#my MODs
import ModinkyStartupImage

#Program called but ChooseAProgram
def ReadDictionary():
    #Prints Dictionary Start up screen
    ModinkyStartupImage.StarUpDictionary()
    while True:
        # gets word to look up or quit command
        word = input('word: ')
        if word in ['Quit']:
            break
        else:
            #opens dictionary (ConlangDatabase.txt) for search
            with open('/home/pi/Desktop/MyCode/LanguageProject/ConlangDatabase.txt', 'r') as f:
                lines = [line.replace('\n', '') for line in f.readlines()]
            
            #boilerplate code for ink pHAT
            inky_display = InkyWHAT("red")
            inky_display.set_border(inky_display.WHITE)
            
            #screen dimension variable
            img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
            draw = ImageDraw.Draw(img)
            
            #searches for the word then returns the next line (Definition) as a str
            i = lines[lines.index(word) + 1]
            ii = lines[lines.index(word) + 2]
            iii = lines[lines.index(word) + 3]
            if word.endswith('t') is True:
                iv = lines[lines.index(word) + 46]
            else:
                iv = lines[lines.index(word) + 5]
            
            #takes str and sets proper variables
                #font select
            fontpath = '/home/pi/Desktop/MyCode/LanguageProject/Fonts/'
            font = ImageFont.truetype(fontpath + 'LinuxLibertinefattened/Linux-Libertine-fattened-Bold.ttf', 25)
                #message construction
            message = word + '\n' + i + '\n' + ii + '\n' + iii + '\n' + iv
                #grid variables: start in top left corner
            x = 0
            y = 0
            
            # uses variables to package str and send to screen
            draw.text((x, y), message, inky_display.RED, font)
            inky_display.set_image(img)
            inky_display.show()