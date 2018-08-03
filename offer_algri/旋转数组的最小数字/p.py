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
    #run:1072ms memory:5053k
    def minNumberInRotateArray2(self, rotateArray):
        if 0 == len(rotateArray): return 0
        return min(rotateArray)
            
    #run:1016ms memory:5704k
    def minNumberInRotateArray(self,rotateArray):
        if 0 == len(rotateArray): return 0
        min_val = rotateArray[0]
        for i in range(len(rotateArray)):
            if rotateArray[i] < min_val:
                min_val = rotateArray[i]
        return min_val