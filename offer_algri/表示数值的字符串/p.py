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
    #run:30ms memory:5450k
    def isNumeric(self, s):
        try:
            float(s)
            if s[0:2] != '-+' and s[0:2] != '+-':
                return True
            else:
                return False
        except:
            return False