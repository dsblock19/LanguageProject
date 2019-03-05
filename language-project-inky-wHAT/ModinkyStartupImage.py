# MOD: Chooses a random glyph to display on startup, displays start up image for each of the four programs

#tools for inky e-paper screen
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

#other tools
import random

#boilerplate set up
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

#creates a variable for each glyph
startupimgGen = Image.open("/home/pi/Desktop/MyCode/E-Paper/istothsymbol.png")
startupimgD = Image.open("/home/pi/Desktop/MyCode/E-Paper/Dglyph.png")
startupimgT = Image.open("/home/pi/Desktop/MyCode/E-Paper/Tglyph.png")
startupimgCQU = Image.open("/home/pi/Desktop/MyCode/E-Paper/CQUglyph.png")
startupimgK = Image.open("/home/pi/Desktop/MyCode/E-Paper/Kglyph.png")
startupimgZ = Image.open("/home/pi/Desktop/MyCode/E-Paper/Zglyph.png")
startupimgAW = Image.open("/home/pi/Desktop/MyCode/E-Paper/AWglyph.png")
startupimgN = Image.open("/home/pi/Desktop/MyCode/E-Paper/Nglyph.png")

#list of all glyph variables
StartUpImg = [startupimgN, startupimgGen, startupimgD, startupimgT, startupimgCQU, startupimgK, startupimgZ, startupimgAW]

#randomly selects a glyph yo print
def StartupImage():
    inky_display.set_image(random.choice(StartUpImg))
    inky_display.show()

def StarUpDictionary():
    #screen dimension variable
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    fontpath = '/home/pi/Desktop/MyCode/Fonts-master/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 18)
    #message construction
    dictionarymessage = '\n         Dictionary\n \n \n             Word?'
    #grid variables: start in top left corner
    x = 0
    y = 0

    # uses variables to package str and send to screen
    draw.text((x, y), dictionarymessage, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()
    
def StarUpPrintConDec():
    #screen dimension variable
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    fontpath = '/home/pi/Desktop/MyCode/Fonts-master/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 18)
    #message construction
    condecmessage = '\n         Conjugator\n         Declinator \n \nWord?    ---    Tense?'
    #grid variables: start in top left corner
    x = 0
    y = 0

    # uses variables to package str and send to screen
    draw.text((x, y), condecmessage, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()

def StarUpConjugator():
    #screen dimension variable
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    fontpath = '/home/pi/Desktop/MyCode/Fonts-master/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 18)
    #message construction
    newwordmessage = '\n         New Word\n\n        What is it?\n       Definition?\n       Tense?'
    #grid variables: start in top left corner
    x = 0
    y = 0

    # uses variables to package str and send to screen
    draw.text((x, y), newwordmessage, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()

def StarUpWordGenerator():
    #screen dimension variable
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    fontpath = '/home/pi/Desktop/MyCode/Fonts-master/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 18)
    #message construction
    wordgenmessage = '\n     Word Generator\n         Command?\n \n    Go: a   ---   Quit: e'
    #grid variables: start in top left corner
    x = 0
    y = 0

    # uses variables to package str and send to screen
    draw.text((x, y), wordgenmessage, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()
