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
    #run:28ms memory:5732k
    def FirstNotRepeatingChar(self, s):  
        if len(s) <= 0:
            return -1
        hash_dict = {}
        for  i in s:
            if i in hash_dict:
                hash_dict[i] += 1
            else:  
                hash_dict[i] = 1
        for j in s:  
            if hash_dict[j] == 1:
                return s.index(j)