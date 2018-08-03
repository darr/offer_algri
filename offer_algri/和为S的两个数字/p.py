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
    #run:32ms memory:5728k
    def FindNumbersWithSum(self,array,tsum):
        if array == None or len(array)<=0 or array[-1] + array[-2] < tsum:
            return []
        start = 0
        end = len(array) - 1
        while start < end:
            s = array[start] + array[end]
            if s < tsum:
                start += 1
            elif s > tsum:
                end -= 1
            else:
                return [array[start],array[end]]
        return []