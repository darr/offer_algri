#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : p.py
# Create date : 2018-07-23 08:49
# Modified date : 2018-07-23 13:04
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################

class Solution:
    #run:330ms memory:5740k
    def Find(self, target, array):
        lenX = len(array)
        lenY = len(array[0])
        m = lenX - 1
        i = 0 
        while m >= 0 and i < lenY :
            if array[m][i] > target:
                m -= 1
            elif array[m][i] < target:
                i += 1
            else:
                return True
        return False