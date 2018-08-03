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
    def GetNumberOfK(self, data, k):
        if data == None or data == []:
            return 0
        if len(data) == 1 and k!=data[0]:
                return 0
        lenA = len(data)
        count = 0
        if data[lenA/2] > k:
            return self.GetNumberOfK(data[:lenA/2],k)
        elif data[lenA/2] < k:
            return self.GetNumberOfK(data[lenA/2:],k)
        else:
            for i in range(lenA/2,lenA):
                if data[i] == k:
                    count +=1
                else:
                    break
            for i in range(lenA/2-1,-1,-1):
                if data[i] == k:
                    count +=1
                else:
                    break
        return count