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
    #run:27ms memory:5680k
    def jumpFloorII(self, number):
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        i = 3
        lt = []
        lt.append(1)
        lt.append(2)
        while i<=number:
            ret = 0
            for j in range(len(lt)):
                ret = ret + lt[j]
            ret +=1
            lt.append(ret)
            i +=1
        return lt[number-1]