#imports
from pynput.keyboard import Key, Controller
import urllib.request
import re
import time
import random
#import sandbox
import pyscreenshot 
import cv2
import pytesseract
import os

#setting critical values, directories and parameters. Also aliasing some stuff
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' 
keyboard = Controller()
postmemesSubList = ["f", "r", "i", "c", "k"]
timescale = 1

#sets the start delay
def introProgram():
    print("Click into Discord now!")
    print("Starting in:")
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    return()

#create functions for different actions

#checks the best option for the "search" command
#this function only chooses options with 0% mortality rate
#the function also prioritises higher income options
#the function will return the best option as string format
#if no oftion is possible, the function will return none as string
def best_option():
    #define low risk options and order by reward
    low_risk_options = ["dresser", "coat", "mailbox", "pantry", "grass", "shoe", "laundromat", "pocket", "bed", "couch", "sink", "car", "bus "]

    #set screenshot location and area
    #note!! these settings only works on 1920x1200 displays, with discord i full screen window
    image = pyscreenshot.grab(bbox=(386, 1050, 598, 1066)) 
    
    #uncomment this to open the screenshot. This is useful for adjusting to different screen resulutions
    #note that this will switch windows away from discord, breaking the bot
    #image.show() 
    
    #saving the screenshot
    image.save("temp.png") 
    
    #opening the saved image and running tesseract ocr.
    img = cv2.imread('temp.png')
    text = (pytesseract.image_to_string(img)).replace(",", "")[:len((pytesseract.image_to_string(img)).replace(",", "")) - 2]
    #text = text[:len(text) - 2]
    print("Options are: " + text)
    #checking the string for matches to low_risk_options
    bestoption = "none"
    for i in range(len(low_risk_options)):
        if (low_risk_options[i]) in text:
            print("Best option = " + low_risk_options[i])
            bestoption = str(low_risk_options[i])
            print("")
            break
    
    if bestoption == "none":
        print("No safe options was avalible. Skipping......")
        print("")
        
    #delete the image and return result
    os.remove("temp.png")
    return(bestoption)

#this function issues the beg command with no return value
def beg():
    for char in "pls beg":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    return()

#this function posts meme with an random option
#the function returns nothing 
def postmeme():
    postmemeSub = random.choice(postmemesSubList)
    for char in "pls postmemes":

        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(1)

    for char in "{}".format(random.choice(postmemesSubList)):

            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    return()


#this function deposits the max amount allowed to you
def deposit():
    for char in "pls deposit max":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

#this function issues the search command. 
#it makes use of best_option to find the best possible option to choose
def search():
    for char in "pls search":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1.5)

    for char in best_option():
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

#delays for commands
# beg: 45
# postmeme: 60
# search: 30

#execution times for commands in seconds
 # beg: 1
 # postmeme: 3
 # search: 8
 # deposit: 1
introProgram()
while True:
    beg()
    postmeme()
    search()
    deposit()
    time.sleep(25 * timescale)
    search()
    time.sleep(13 * timescale)
    beg()
    deposit()
    time.sleep(13 * timescale)
    postmeme()
    search()
    deposit()
    time.sleep(23 * timescale)
    beg()
    search()
    time.sleep(30 * timescale)
    search()
    postmeme()
    time.sleep(12 * timescale)
    beg()
    time.sleep(18 * timescale)
    search()
    time.sleep(26 * timescale)

    


