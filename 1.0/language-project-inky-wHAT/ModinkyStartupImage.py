# MOD: Chooses a random glyph to display on startup, displays start up image for each of the four programs

#tools for inky e-paper screen
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw

#other tools
import random

#boilerplate set up
inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

#creates a variable for each glyph
startupimgGen = Image.open("/home/pi/Desktop/MyCode/LanguageProject/E-Paper/istothsymbol.png")
startupimgD = Image.open("/home/pi/Desktop/MyCode/LanguageProject/E-Paper/Dglyph.png")
startupimgT = Image.open("/home/pi/Desktop/MyCode/LanguageProject/E-Paper/Tglyph.png")
startupimgCQU = Image.open("/home/pi/Desktop/MyCode/LanguageProject/E-Paper/CQUglyph.png")
startupimgK = Image.open("/home/pi/Desktop/MyCode/LanguageProject/E-Paper/Kglyph.png")
startupimgZ = Image.open("/home/pi/Desktop/MyCode/LanguageProject/E-Paper/Zglyph.png")
startupimgAW = Image.open("/home/pi/Desktop/MyCode/LanguageProject/E-Paper/AWglyph.png")
startupimgN = Image.open("/home/pi/Desktop/MyCode/LanguageProject/E-Paper/Nglyph.png")

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
    fontpath = '/home/pi/Desktop/MyCode/LanguageProject/Fonts/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 35)
    #message construction
    dictionarymessage = '\n\n\n         Dictionary\n \n \n \n \n \n            Word?'
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
    fontpath = '/home/pi/Desktop/MyCode/LanguageProject/Fonts/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 35)
    #message construction
    condecmessage = '\n\n         Conjugator\n\n\n         Declinator \n \n \n  Word?  ---  Tense?'
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
    fontpath = '/home/pi/Desktop/MyCode/LanguageProject/Fonts/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 35)
    #message construction
    newwordmessage = '\n\n\n         New Word\n\n\n\n        What is it?\n\n       Definition?\n\n       Tense?'
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
    fontpath = '/home/pi/Desktop/MyCode/LanguageProject/Fonts/'
    font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 35)
    #message construction
    wordgenmessage = '\n\n\n     Word Generator\n\n\n         Command?\n \n \n     Go   ---   Quit'
    #grid variables: start in top left corner
    x = 0
    y = 0

    # uses variables to package str and send to screen
    draw.text((x, y), wordgenmessage, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()