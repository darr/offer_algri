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
    #run:30ms memory:5712k
    def IsContinuous(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return False
        transDict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in transDict.keys():
                numbers[i] = transDict[numbers[i]]
        numbers = sorted(numbers)
        numberOfzero = 0
        numberOfGap = 0
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            numberOfzero += 1
            i += 1
        small = numberOfzero
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            numberOfGap += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return False if numberOfGap > numberOfzero else True
