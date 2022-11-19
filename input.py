'''  Function to Read in Files for Parsing
     Emma Sommers
     11/19/22
'''


import os
import sys
import parse



def read_and_send():
    ''' Call this function to read in all files, and send their contents one at a time to the parser from tulasi  '''
    files = read_files()
    for file in files:
        parse.parse(get_contents(file))

def read_files():
    ''' Function to return list of .py files in the current directory '''
    return [file for file in os.listdir(sys.argv[1]) if '.py' == file[-3:]]

def get_contents(file):
    ''' Read in 1 file and return its contents as a list of string '''
    with open(os.path.join(sys.argv[1], file), 'r') as infile:
        return infile.readlines()
