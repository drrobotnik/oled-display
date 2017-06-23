import RPi.GPIO as GPIO

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

with open('words.log') as f:
    content = f.readlines()

content = [x.strip() for x in content]
list_len = len(content)
current_index = 0
previous_text = ""
def direction_push(channel) :
    global current_index

    if U_pin == channel :
        print 'up'
        current_index = current_index - 1
    elif D_pin == channel :
        print 'down'
        current_index = current_index + 1

    print current_index


    if current_index > list_len :
        current_index = list_len

    if current_index < 0 :
        current_index = 0

    draw.text((x, top), str(content[current_index]),  font=font, fill=255)
    print content[current_index]


def get_count() :
    global current_index
    return current_index

def set_count(new_count) :
    global current_index
    global list_len

    if( new_count >= list_len ) :
        new_count = list_len

    if ( new_count <= 0 ) :
        new_count = 0

    current_index = new_count
    return new_count

def count_up(obj) :
    global previous_text
    curr_count = get_count()
    previous_text = content[curr_count]
    update_count = set_count( curr_count + 1 )
    print update_count
    get_text_from_count(update_count)

def count_down(obj) :
    global previous_text
    curr_count = get_count()
    previous_text = content[curr_count]
    update_count = set_count( curr_count - 1 )
    print update_count
    get_text_from_count(update_count)

def get_text_from_count(count) :
    global previous_text
    draw.text((x, top), str(previous_text),  font=font, fill=0)
    draw.text((x, top), str(content[count]),  font=font, fill=255)
    print content[count]
    disp.display()

# Input pins:
L_pin = 21 
R_pin = 12 
C_pin = 6 
U_pin = 26 
D_pin = 16 

A_pin = 5 
B_pin = 6 


GPIO.setmode(GPIO.BCM) 

# GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
# GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
x = 0
top = -2

# Load default font.
font = ImageFont.load_default()

GPIO.add_event_detect(U_pin, GPIO.FALLING, callback=count_up, bouncetime=300)
GPIO.add_event_detect(D_pin, GPIO.FALLING, callback=count_down, bouncetime=300)

try:
    while 1:
#        if GPIO.input(U_pin): # button is released
#            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  #Up
#        else: # button is pressed:
#            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)  #Up filled
#
#        if GPIO.input(L_pin): # button is released
#            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  #left
#        else: # button is pressed:
#            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=1)  #left filled
#
#        if GPIO.input(R_pin): # button is released
#            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0) #right
#        else: # button is pressed:
#            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=1) #right filled
#
#        if GPIO.input(D_pin): # button is released
#            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0) #down
#        else: # button is pressed:
#            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=1) #down filled
#        if GPIO.input(C_pin): # button is released
#            draw.rectangle((20, 22,40,40), outline=255, fill=0) #center 
#        else: # button is pressed:
#            draw.rectangle((20, 22,40,40), outline=255, fill=1) #center filled
#
#        if GPIO.input(A_pin): # button is released
#            draw.ellipse((70,40,90,60), outline=255, fill=0) #A button
#        else: # button is pressed:
#            draw.ellipse((70,40,90,60), outline=255, fill=1) #A button filled

#        if GPIO.input(B_pin): # button is released
#            draw.ellipse((100,20,120,40), outline=255, fill=0) #B button
#        else: # button is pressed:
#            draw.ellipse((100,20,120,40), outline=255, fill=1) #B button filled
#
#        if not GPIO.input(C_pin):
#            catImage = Image.open('happycat_oled_32.ppm').convert('1')
#            disp.image(catImage)
#        else:
#            # Display image.
#            disp.image(image)
#
        disp.display()
        time.sleep(.01) 


except KeyboardInterrupt: 
    GPIO.cleanup()
