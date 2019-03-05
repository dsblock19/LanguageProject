from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.open("/home/pi/Desktop/MyCode/E-Paper/istothsymbol.png")
inky_display.set_image(img)
inky_display.show()