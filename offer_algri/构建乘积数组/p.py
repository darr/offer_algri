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
    #run:29ms memory:5736k
    def multiply(self,A):
        if A == None or len(A) == 1:
            return A
        lenA = len(A)
        lt = [1]*lenA
        for i in range(1,lenA):
            lt[i] = lt[i-1]*A[i-1]
        temp = 1
        for j in range(lenA-2,-1,-1):
            temp *= A[j+1]
            lt[j] *= temp
        return lt
