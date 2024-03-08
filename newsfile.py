#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 19:08:11 2024

@author: spencerharris
"""

# Put mysay.py in the same folder as this script
from mysay import print_say
import pathlib

# Open the file, and read the content of the text file
myfile = pathlib.Path.cwd() / 'files' / 'storm.txt'
with open(myfile,'r') as f:
    content = f.read()
# Let Python speak the text in the file   
print_say(content)