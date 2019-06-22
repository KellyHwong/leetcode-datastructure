#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: kelly hwong
# Date: April 2019

def isIn(str1, str2):
    for c in str1:
        if c in str2:
            pass
        else:
            return False
    return True

str1 = ["e", "o"]
str2 = "facebook"
print(isSubset(str1, str2))

