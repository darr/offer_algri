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
   #run:23ms memory:5728k 
    def Sum_Solution(self,n):
        fun = {False: self.sum0, True: self.sumN}
        return fun[not not n](n)

    def sum0(self, n):
        return 0

    def sumN(self, n):
        fun = {False: self.sum0, True: self.sumN}
        return n + fun[not not n](n - 1)