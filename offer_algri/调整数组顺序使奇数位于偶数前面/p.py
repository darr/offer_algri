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
    #run:22ms memory:5740k
    def reOrderArray(self, array):
        lt = []
        lenA = len(array)
        for i in range(lenA):
            if array[i] % 2 !=0:
                lt.append(array[i])
        for i in range(lenA):
            if array[i] % 2 == 0:
                lt.append(array[i])
        return lt