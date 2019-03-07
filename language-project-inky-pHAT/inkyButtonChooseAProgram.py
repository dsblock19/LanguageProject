#top level program: python3 /home/pi/Desktop/MyCode/LanguageProject/language-project-inky-pHAT/inkyButtonChooseAProgram.py &

#tools for inky e-paper screen
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

#tools for button/LED SHIM
import buttonshim
import signal

#My MODs
import ModinkyStartupImage
import ModinkyWordConjugator
import ModinkyWordGenerator
import ModinkyReadDictionary
import ModinkyPrintConDec


#inky boilerplate set up
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

#inky screen dimension variables
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

#set up font
fontpath = '/home/pi/Desktop/MyCode/LanguageProject/Fonts/'
font = ImageFont.truetype(fontpath + 'SF-Outer-Limits.ttf', 18)


#set up startup message
startupmessage = '\n      istoth:\nLanguage in Stone\n \n \n      Which program?'
x = 0
y = 0

buttonshim.set_pixel(0xff, 0x00, 0x00)
#ModinkyStartupImage.StartupImage()

while True:
    #turns light red while screen is getting set
    buttonshim.set_pixel(0xff, 0x00, 0x00)
    #draws start up message on inky
    draw.text((x, y), startupmessage, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()
    #turns light green to signal ready for button input
    buttonshim.set_pixel(0x00, 0xff, 0x00)
    
    #button input options
    @buttonshim.on_press(buttonshim.BUTTON_A)
    def button_a(button, pressed):
        buttonshim.set_pixel(0xff, 0x00, 0x00)
        ModinkyReadDictionary.ReadDictionary()

    @buttonshim.on_press(buttonshim.BUTTON_B)
    def button_b(button, pressed):
        buttonshim.set_pixel(0xff, 0x00, 0x00)
        ModinkyPrintConDec.inkyPrintDictionary()

    @buttonshim.on_press(buttonshim.BUTTON_C)
    def button_c(button, pressed):
        buttonshim.set_pixel(0xff, 0x00, 0x00)
        ModinkyWordConjugator.NewWord()

    @buttonshim.on_press(buttonshim.BUTTON_D)
    def button_d(button, pressed):
        buttonshim.set_pixel(0xff, 0x00, 0x00)
        ModinkyWordGenerator.WordGenerator()

    
    #pauses program to wait for signal
    signal.pause()