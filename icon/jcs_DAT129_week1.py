"""
Jason Swart
    Sat Feb 08 2020 - updated and uploaded Mon Feb 17 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 1
    Icon Processing
    
    This is my fourth attempt to get this script to work. Previous versions based
    off of the pseudo-code discussed with partner were unsuccessful - I could not
    get any part of them to work after an initial tech problem. In an effort to 
    actually turn an assignment in I have simplified this as much as possible to 
    achieve the assigned result. 
"""

# importing 'contextlib' for later use in redirecting the output of the functions 
# to a text file.

import contextlib

#Binary interpretation of chosen icon, music notes with a line running through,
#input into a dictionary to maniuplation and output by script.

iconbits = {"line 1" :[0,0,0,0,0,0,0,0,0,0],
            "line 2" :[0,0,0,1,1,1,1,1,0,0],
            "line 3" :[0,0,0,1,0,0,0,1,0,0],
            "line 4" :[0,0,0,1,0,0,0,1,0,0],
            "line 5" :[1,1,1,1,1,1,1,1,1,1],
            "line 6" :[0,0,0,1,0,0,0,1,0,0],
            "line 7" :[0,0,1,1,0,0,1,1,0,0],
            "line 8" :[0,1,0,1,0,1,0,1,0,0],
            "line 9" :[0,0,1,1,0,0,1,1,0,0],
            "line 10" :[0,0,0,0,0,0,0,0,0,0]}

# iconprint function iterates over the dictionary and converts characters from 
# binary into printable "@" symbol for "1" and empty space for "0".

def iconprint():
    for key in iconbits:
        binarylst = iconbits[key]

        for value in binarylst:
            if value == 1:
                print("@", end=" ")
            else:
                print(" ", end=" ")
        print(" ")
 
# reflection function flips the icon horizontally reverses the character conversion
# so that "1" becomes the empty space and "0" becomes the "@" symbol.
       
def flipicon():
    for key in iconbits:
        binarylst = iconbits[key]
        binarylst.reverse()
        for value in binarylst:
            if value == 1:
                print(" ", end=" ")
            else:
                print("@", end=" ")
                
        print(" ")

# function to print the icon in both its proper and flipped forms to a text file.
# function also asks the user to name the text file. If no response is given, a 
# default filename is provided.
        
def printable():
    iconName = input("This program will generate a text file of the following icon.\n"
                     "What would you like to name it?: ") or 'icon.txt'
    with open(iconName + '.txt', 'w') as f:
        with contextlib.redirect_stdout(f):
            iconprint()
            flipicon()
       
# main function calls the previous functions and prints them to the console in 
# readable format.
             
def main(iconbits):
    
    printable()
    iconprint()
    print(" ")
    flipicon()

    
main(iconbits)