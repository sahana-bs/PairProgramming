# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 12:05:18 2022

Roman to Integer

@author: Disha Bhan
IDE: Spyder

"""


def romanToInt(s):
    '''Function to convert Roman to Integer'''  
    # Creating a dictionary for mapping roman to integer
    dict_l = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}

    # if length of string is 1 return the value
    if len(s) == 1:
        return dict_l[s[0]] 
    sum = dict_l[s[len(s)-1]]
    
    # looping over the string
    for i in range(len(s)-2, -1, -1):
            # preceding roman nummber is smaller
            # we need to undo the previous addition
            # and substract the preceding roman char
            if dict_l[s[i]] >= dict_l[s[i+1]]:
                sum += dict_l[s[i]]
            else:
                sum -= dict_l[s[i]]

    return sum

