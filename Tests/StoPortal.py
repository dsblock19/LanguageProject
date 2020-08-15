#TASK: Get/Display Weight

#LIBRARIES
#Display
import displayio
#PyPortal
from analogio import AnalogIn
import neopixel
import adafruit_adt7410
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text.label import Label
from adafruit_button import Button
import adafruit_touchscreen
from adafruit_pyportal import PyPortal
#Time Tools
import time
import board
import storage
import adafruit_sdcard
import os
import digitalio
import busio


#SETUP

#PyPortal and PyPortal Setup Functions
#Display
#pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=1)
WHITE = 0xffffff
RED = 0xff0000
YELLOW = 0xffff00
GREEN = 0x00ff00
BLUE = 0x0000ff
PURPLE = 0xff00ff
BLACK = 0x000000
pyportal = PyPortal()
display = board.DISPLAY
display.rotation=0
# Backlight function
# Value between 0 and 1 where 0 is OFF, 0.5 is 50% and 1 is 100% brightness.
def set_backlight(val):
    val = max(0, min(1.0, val))
    board.DISPLAY.auto_brightness = False
    board.DISPLAY.brightness = val
set_backlight(0.3)
#Touchscreen
screen_width = 320
screen_height = 240
ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      calibration=((5200, 59000), (5800, 57000)),
                                      size=(screen_width, screen_height))
#Display Groups
splash = displayio.Group(max_size=20)  # The Main Display Group
view1 = displayio.Group(max_size=20)  # Group for View 1 objects
view3 = displayio.Group(max_size=20)  # Group for View 3 objects
splash.append(view1)
#Show/Hide Layer Funcs.
def hideLayer(hide_target):
    try:
        splash.remove(hide_target)
    except ValueError:
        pass
def showLayer(show_target):
    try:
        time.sleep(0.1)
        splash.append(show_target)
    except ValueError:
        pass
#Images
# Display an image until the loop starts
pyportal.set_background('/images/PortalBackground.bmp')
bg_group = displayio.Group(max_size=1)
splash.append(bg_group)
icon_group = displayio.Group(max_size=1)
icon_group.x = 180
icon_group.y = 120
icon_group.scale = 1
# This will handel switching Images and Icons
def set_image(group, filename):
    """Set the image file for a given goup for display.
    This is most useful for Icons or image slideshows.
        :param group: The chosen group
        :param filename: The filename of the chosen image
    """
    print("Set image to ", filename)
    if group:
        group.pop()
    if not filename:
        return  # we're done, no icon desired
    if not filename:
        return  # we're done, no icon desired
    image_file = open(filename, "rb")
    image = displayio.OnDiskBitmap(image_file)
    try:
        image_sprite = displayio.TileGrid(image, pixel_shader=displayio.ColorConverter())
    except TypeError:
        image_sprite = displayio.TileGrid(image, pixel_shader=displayio.ColorConverter(),
                                          position=(0, 0))
    group.append(image_sprite)
#Run Image Switch Function
#set_image(bg_group, "/images/BackGround.bmp")
#Font
# Set the font and preload letters
font = bitmap_font.load_font("/fonts/SourceSerifPro-Bold-17.bdf")
font.load_glyphs(b'acdeghilmorstuvxyALMRTW1234567890- ()!')
#Text Boxes
# Default Label styling:
TABS_X = 10
TABS_Y = 50
# Text Label Objects
#Screen Label
'''
sensors_label = Label(font, text="Words, Words, Words:", color=PURPLE, max_glyphs=200)
sensors_label.x = TABS_X
sensors_label.y = TABS_Y
view3.append(sensors_label)
'''
 #Data Label
sensor_data = Label(font, text="Data View", color=0x03AD31, max_glyphs=150)
sensor_data.x = TABS_X #+ 10
sensor_data.y = TABS_Y #+ 40
view3.append(sensor_data)
text_hight = Label(font, text="M", color=0x03AD31, max_glyphs=10)
# return a reformatted string with word wrapping using PyPortal.wrap_nicely
def text_box(target, top, string, max_chars):
    text = pyportal.wrap_nicely(string, max_chars)
    new_text = ""
    test = ""
    for w in text:
        new_text += '\n'+w
        test += 'M\n'
    text_hight.text = test  # Odd things happen without this
    glyph_box = text_hight.bounding_box
    target.text = ""  # Odd things happen without this
    target.y = int(glyph_box[3]/2)+top
    target.text = new_text

def switch_view():
    hideLayer(view1)
    showLayer(view3)
    print("View3 On")

def ScreenStuff(row):
    #try:
    #Format Readings Into String
    print('Coverting Text')
    row = row.split(',')
    row = str(row[0] + '\n\n  Def: ' + row[1] + '\n\nPart of Speech: ' + row[2])
    row = row.replace('"','')
    row = row.replace(';',';\n      ')
    sensor_data.text = row
    #Display Feed Data
    print('Switch View')
    switch_view()
    print('\nWait\n')
    time.sleep(4)
    scrn = 1


#Run Image Switch Function
set_image(bg_group, "/images/PortalBackgroundII.bmp")

#Display Layer Initial Position
showLayer(view1)
hideLayer(view3)

# Update out Labels with display text.
board.DISPLAY.show(splash)

#LOOP
while True:
    with open('/sd/Sto.csv', 'r') as Dcsv:
        for row in Dcsv:
            print(row)
            ScreenStuff(row)
            time.sleep(10)
