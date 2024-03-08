#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 18:58:06 2024

@author: spencerharris
"""
# Put mysr.py and mysay.py in the same folder as this script
from mysr_copy import voice_to_text
from mysay import print_say

while True:   
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print_say(f'You just said {inp}, goodbye!')
        break
    else:
        print_say(f'You just said {inp}')
        continue 
