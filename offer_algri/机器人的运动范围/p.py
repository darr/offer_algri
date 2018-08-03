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
    def movingCount(self, threshold, rows, cols):
        visited = [False] * (rows * cols)
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)
        return count
    
    def get_digit_sum(self,num):
        bit_sum = 0
        while num > 0:
            bit_sum += num%10
            num = num//10
        return bit_sum

    def movingCountCore(self,threshold,rows,cols,row,col,visited):
        count = 0
        if row >= 0 and col >= 0 \
        and row < rows and col < cols \
        and self.get_digit_sum(row) + self.get_digit_sum(col) <= threshold \
        and not visited[row*cols + col]:
            visited[row*cols+col] = True
            count = 1 + self.movingCountCore(threshold, rows, cols, row-1, col, visited) + \
                        self.movingCountCore(threshold, rows, cols, row+1, col, visited) + \
                        self.movingCountCore(threshold, rows, cols, row, col-1, visited) + \
                        self.movingCountCore(threshold, rows, cols, row, col+1, visited)
        return count

