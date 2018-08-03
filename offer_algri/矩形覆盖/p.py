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
    def rectCover(self, number):
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        i = 3
        f_1 = 1
        f_2 = 2
        ret = None
        while i<=number:
            ret = f_1 + f_2
            f_1 = f_2
            f_2 = ret
            i += 1
        return ret