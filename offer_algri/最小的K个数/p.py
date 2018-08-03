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
    #run:33ms memory:5732k
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <=0:
            return []
        list_size = len(tinput)
        start = 0
        end = list_size - 1
        index = self.QuickSelect(tinput, list_size, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.QuickSelect(tinput, list_size, start, end)
            else:
                start = index + 1
                index = self.QuickSelect(tinput, list_size, start, end)
        output = tinput[:k]
        output.sort()
        return output
    
    def QuickSelect(self,numbers,length,start,end):
        if numbers == None or length <= 0 or start < 0 or end >= length:
            return None
        if end == start:
            return end
        pivotvlue = numbers[start]
        leftmark = start + 1
        rightmark = end
        while True:
            while numbers[leftmark] <= pivotvlue and leftmark <= rightmark:
                leftmark += 1
            while numbers[rightmark] >= pivotvlue and rightmark >= leftmark:
                rightmark -= 1
            if leftmark >= rightmark:
                break
            else:
                numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]
        numbers[rightmark], numbers[start] = numbers[start], numbers[rightmark]
        return rightmark