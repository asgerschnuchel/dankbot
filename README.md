# dankbot
A bot for the DankMemer discord bot.
The bot is designed to be run in client, through VSCode, Python shell or likewise.
The bot uses an combination of pytesseract, cv2 and pynput to implement all functionallity
As far as i know, this is the only dank memer bot to incorporate support for the search function, with "smart choice"
The bot will only pick options with 100% mortallity rate. If there is more than 1 safe option avalible, the bot will choose the option with highest possible payout.
If there is no safe options avalible, the bot will merely skip and continue normal operation.

The bot has the following requirements:
tesseract must be installed on the system
pytesseract
cv2
pyscreenshot
pynput

How to use the bot:
Make sure that the path on ln14 points to the directory in which tesseract is installed, otherwise the program will not function!!
The bot is really simple to use. 
Just open your favorite IDE or teminal that supports python execution.
Run the program, and set your cursor in the xhat field in discord, in the channel which the bot operates.
Note that the search function can be interrupted if an message is sent by another person at the right time window.
Discord must be on the computers main display.
The bot is optimized to not run into the time limits and cooldowns. The bot is optimized for non paid cooldown.
If you should encounter any issues with running into cooldowns, increase the timescale value on ln17 in increments of 0.1

Notes and issues
The bot does currently only work on 1920x1200 screen resolution.
This will be fixed at a later time.


