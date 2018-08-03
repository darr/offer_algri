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
    def StrToInt(self, s):
        lt = list(s)
        b = 1
        s = 0
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in range(len(lt)-1,-1,-1):
            if i != 0:
                v = dict.get(lt[i],-1)
                if v > -1:
                    s +=  (v * b)
                else:
                    return 0
                b *= 10
            else:
                if lt[i] == '-':
                    s = 0 - s
                elif lt[i] == '+':
                    pass
                else:
                    v = dict.get(lt[i],-1)
                    if v > -1:
                        s +=  (v * b)
                    else:
                        return 0
        return s