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
    #run:26ms memory:5628k
    def FindContinuousSequence(self, tsum):
        lt = []
        for i in range(tsum,1,-1):
            if (2*tsum - i *(i-1)) % (2*i) == 0:
                a = (2*tsum - i *(i-1)) / (2*i)
                if a>0:
                    l = []
                    for j in range(i):
                        l.append(a+j)
                    lt.append(l)
        return lt