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
    #run:28ms memory:5620k
    def FindGreatestSumOfSubArray(self, array):
        if array == None or len(array) <= 0:
            return 0
        max_sum = array[0]
        cur_sum = 0
        for item in array:
            if cur_sum < 0:
                cur_sum = item
            else:
                cur_sum += item
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum