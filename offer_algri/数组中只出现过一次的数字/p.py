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


    def FindNumsAppearOnce(self, array):
        if array == None or len(array) <= 0:
            return []
        resultExOr = self.ExOr(array)
        i = 0
        while resultExOr and i <= 32:
            i += 1
            resultExOr = resultExOr>>1
        num1, num2 = [], []
        for num in array:
            if self.bitIs1(num, i):
                num1.append(num)
            else:
                num2.append(num)
        first = self.ExOr(num1)
        second = self.ExOr(num2)
        return [first, second]

    def ExOr(self, aList):
        ExOrNum = 0
        for i in aList:
            ExOrNum = ExOrNum ^ i
        return ExOrNum
        
    def bitIs1(self, n, i):
        n = n >> (i-1)
        return n & 1
