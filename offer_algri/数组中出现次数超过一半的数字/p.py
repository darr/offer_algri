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
    #run:32ms memorry:5624k
    def MoreThanHalfNum_Solution(self,numbers):
        lenN = len(numbers)
        if numbers == None or lenN <= 0:
            return 0
        num = numbers[0]
        times =1
        for i in range(1,lenN):
            if times == 0:
                num = numbers[i]
            elif numbers[i] == num:
                times +=1
            else:
                times -=1
                
        count = 0
        for i in range(lenN):
            if numbers[i] == num:
                count +=1
                if count > lenN/2:
                    return num
        return 0