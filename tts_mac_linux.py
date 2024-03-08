#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 18:34:16 2024

@author: spencerharris
"""

import os

while True: 
    inp = input("What do you want to covert to speech?\n") 
    if inp == "done": 
        print(f"You just typed in {inp}; goodbye!")
        os.system(f'gtts-cli --nocheck "You just typed in {inp}; goodbye!" | mpg123 -q -')
        break
    else: 
        print(f"You just typed in {inp}")
        os.system(f'gtts-cli --nocheck "{inp}" | mpg123 -q -')
        continue 