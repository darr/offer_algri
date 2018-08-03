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


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []
         
    def push(self, node):
        self.stk1.append(node)
         
    def pop(self):
        if self.stk2 == []:
            while self.stk1:
                n = self.stk1.pop()
                self.stk2.append(n)
        n = self.stk2.pop()
        return n