# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:26:55 2020

@author: AAYUSH MISHRA
"""

import re
from termcolor import cprint

pwd = input('Check your password here: ')

passwordRegex = re.compile(r'''(
        ^
        (?=.*[A-Z])
        (?=.*[a-z])
        (?=.*[0-9])
        (?=.*[!?@.*^%])
        [a-zA-Z0-9!?@.*^%]
        {8,}
        $
        )''', re.VERBOSE)

check = passwordRegex.search(pwd)

if not(check):
    cprint('\n\n\t\t\tHEY NOOBIE, YOUR PASSWORD IS WEAK!!', 'red', attrs=['bold','blink'])
    cprint('''
                         Try including the following:
                             At least 1 uppercase letter
                             At least 1 lowercase letter
                             At least 1 number
                             At least 1 special character
                             At least 8 characters long
          ''', 'red', attrs=['bold','blink'])
else:
    cprint('\n\t\t\tSTRONG AND LONG, YOU\'RE GOOD TO GO!!', 'blue', attrs=['bold','blink'])