#Core: takes input and reads entry based on input for inky pHAT

#tools
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

#retrieves definition, formats it and print it on inky
def inkyGetPrintDef():
    #boilerplate code for ink pHAT
    inky_display = InkyPHAT('red')
    inky_display.set_border(inky_display.WHITE)
    #screen dimension variable
    img = Image.new('P', (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    
    #searches for the word then returns the next line (Definition) as a str
    i = lines[lines.index(word) + 1]
    #takes that str and sets proper variables
        #font select
    fontpath = '/home/pi/Desktop/MyCode/Fonts/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 17)
        #message construction
    message = '     '+ word + '\n' + i
        #grid variables: start in top left corner
    x = 0
    y = 0
    # uses variables to package str and send to screen
        #
    draw.text((x, y), message, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()

#core program
while True:
        # gets word to look up or quit command
        word = input('word: ')
        if word in ['Quit']:
            break
        else:
            #opens dictionary (ConlangDatabase.txt) for search
            with open('/home/pi/Desktop/ConlangDatabase.txt', 'r') as f:
                lines = [line.replace('\n', '') for line in f.readlines()]
            inkyGetPrintDef()