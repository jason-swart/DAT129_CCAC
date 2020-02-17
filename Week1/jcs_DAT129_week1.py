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

# main function calls the previous functions and prints them to the console in 
# readable format.
             
def main(iconbits):
    
    iconprint()
    print(" ")
    flipicon()

# Attempted code to output the script into a text file. As yet not working.    
#with open("week1_icon.txt", "w") as f:
#    f.write(str(main(iconbits)))
    
main(iconbits)