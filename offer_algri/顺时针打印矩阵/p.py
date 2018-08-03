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
    #run:33ms memory:5712k
    def printMatrix(self, matrix):
        if matrix is None:
            return None
        if matrix is []:
            return []
        r = len(matrix)
        c = len(matrix[0])
        lt = []
        start = 0
        while c > 2 * start and r > 2 * start:
            endX = c - 1 - start
            endY = r - 1 - start
            for i in range(start,endX+1):
                lt.append(matrix[start][i])
            if start < endY:
                for i in range(start+1,endY+1):
                    lt.append(matrix[i][endX])
            if start < endX and start < endY:
                for i in range(endX-1,start-1,-1):
                    lt.append(matrix[endY][i])
            if start < endX and start < endY -1:
                for i in range(endY-1,start,-1):
                    lt.append(matrix[i][start])
            start +=1
        return lt