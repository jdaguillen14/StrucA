# Jose Guillen
# jdg4479
# Struc A Hw: 4
# This file is used as an interface to make running the program easier

import numpy as np

def Top_Simulate():
    a = 'lil thing'
    # Replace the file names to follow this format
    name1 = open('nodes.txt','r')
    name2 = open('elements.txt','r')
    name3 = open('forces.txt','r')
    name4 = open('displacements.txt','r')
    
    # Find the properties of the structure input
    print(name1)
