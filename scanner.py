#!/usr/bin/python3

# Anthony Giacalone
# Assignment 2
# CECS 444
# Baby Scanner

# This will be a port of some C++ code provided
#  by Prof. Konig with some additional conditionals
#  added, modified state/action/lookup tables and
#  a bit different logic. So, basically a complete
#  re-write of the code. But in Python.

# import the tables
from statetable import *
from actiontable import *
from lookuptable import *

# Choose the file to scan
print("Here is the file to scan: ")
scanned_file = open('source.txt').read().strip(' ')  # read in file and strip lead/trail whitespace
print(scanned_file)     # To show the user what we're scanning


# Here starts the main portion of the program
state = 0
token_status = ""
counter = 0
buffered = 0

# A giant while loop. I'll consider changing this to call a class or two, perhaps.
while counter < len(scanned_file):
    token = scanned_file[counter]           # token variable is the actual char input
    
    # compare the various tokens and determine state table value
    if token.isdigit():
        current_read = 0

    elif token == '.':
        current_read = 1

    elif token.isalpha():
        current_read = 2

    elif token == '=':
        current_read = 3

    elif token == '+':
        current_read = 4

    elif token == ';':
        current_read = 5

    elif token == '_':
        current_read = 6

    elif token == '\n':
        current_read = 7    

    elif token.isspace():
        current_read = 7 

    else: current_read = 7
    
    #print("current state =", current_read)
    #print("current char  =", token)
    #print("token status  =", token_status)
    #print("new state     =", statetable.gettable(state, current_read))
    
    if (statetable.gettable(state, current_read) != -1) and (actiontable.gettable(state, current_read) == 1):
        token_status = token_status + token         # token_status is the accumulated chars
        state = statetable.gettable(state, current_read)
        buffered = 0
    
    elif (statetable.gettable(state, current_read) == -1) and (actiontable.gettable(state, current_read) == 2):
        # Halting condition
        #print("inside switch with state = ", state, "and char", current_read)
        #print("The lookup value is = ", lookuptable.gettable(state, current_read))
        #print("We have a buffered character = ", token)
        buffered = 1
        
        # Python doesn't have a switch statement. Go figure.
        if lookuptable.gettable(state, current_read) == 1:
            print("TOKEN DISCOVERED is INT->", token_status)
            
        elif lookuptable.gettable(state, current_read) == 2:
            print("TOKEN DISCOVERED is ID->", token_status)
        
        elif lookuptable.gettable(state, current_read) == 3:
            print("TOKEN DISCOVERED is EQUAL->", token_status)
        
        elif lookuptable.gettable(state, current_read) == 4:
            print("TOKEN DISCOVERED is PLUS->", token_status)

        elif lookuptable.gettable(state, current_read) == 5:
            print("TOKEN DISCOVERED is SEMICOLON->", token_status)
           
        elif lookuptable.gettable(state, current_read) == 6:
            print("TOKEN DISCOVERED is REAL->", token_status)           
            
        else:
            print("error")
        state = 0
        token_status = ""    # clear the token buffer

    if buffered != 1:
        #if token == "\n": print("EOL")             # print EOL for end of line
        counter += 1
    else: buffered = 0
    # end while loop
    
print("Done scanning")       # end of scanner
