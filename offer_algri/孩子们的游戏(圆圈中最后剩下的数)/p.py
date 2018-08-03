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
    def LastRemaining_Solution(self, n, m):
        if n <= 0 or m <= 0:
            return -1
        index = 0
        for i in range(n):
            index = (index + m)%(i+1)
        return index