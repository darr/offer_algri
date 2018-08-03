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
    def Fibonacci(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        i = 3
        f_1 = 1
        f_2 = 1
        ret = None
        while i<=n:
            ret = f_1 + f_2
            f_1 = f_2
            f_2 = ret
            i += 1
        return ret