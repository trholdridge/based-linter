'''
     Function to Read in Files for Parsing and Output Errors from list of Errors 
     Emma Sommers
     11/19/22
'''


import os
import sys

import parse
import warnings


def parse_and_warn():
    ''' Runs program by reading files, sending their contents to be parsed, and printing their warnings  '''
    files = read_files()
    for file in files:
        parsed = parse.parse(get_contents(file))
        printWarnings(warnings.assembleWarning(parsed), file)

def read_files():
    ''' Function to return list of .py files in the current directory '''
    path = sys.argv[1]
    if os.path.isfile(path):
        files = [os.path.abspath(path)]
    elif os.path.isdir(path):
        files = [os.path.join(os.path.abspath(path), file) for file in os.listdir(path)]
    return files

def get_contents(file):
    ''' Read in 1 file and return its contents as a list of string '''
    with open(file, 'r') as infile:
        return infile.readlines()

def printWarnings(warn_list, fname):
    ''' Prints list of Warnings for each file in a list of Warnings  '''
    END = "\033[0m"
    colors = {"Pronouns": "\033[1;35m",
              "Gendered Language": "\033[1;36m",
              "Problem Terms": "\033[1;34m",
              "libraries":"\033[1;32m" }
    for error in warn_list:
        print("File ", fname, ", line ", error.lineNumber, sep='')
        print('\t', colors[error.type], error.type, END, ": ", error.warningMessage, sep='')
