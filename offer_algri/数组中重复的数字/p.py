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
    #run:24ms memory:5860k
    def duplicate(self, numbers, duplication):
        if numbers == None or len(numbers) <2:
            return False
        lt = [0 for i in range(len(numbers))]
        for i in range(len(numbers)):
            lt_item = lt[numbers[i]]
            if lt_item > 0:
                duplication[0] = numbers[i]
                return True
            else:
                lt[numbers[i]] = lt_item + 1
        return False