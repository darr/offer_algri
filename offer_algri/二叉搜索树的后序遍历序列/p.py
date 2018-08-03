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
    #run:22ms memory:5852k
    def VerifySquenceOfBST(self,sequence):
        if sequence == []:
            return False
        if len(sequence) == 1:
            return True
        limit_index = -1
        for i in range(len(sequence)-1):
            if sequence[i] > sequence[-1]:
                limit_index = i
            elif sequence[i] < sequence[-1] and limit_index != -1:
                return  False
        if limit_index != 0 and limit_index != -1:
            left = self.VerifySquenceOfBST(sequence[:limit_index])
            right = self.VerifySquenceOfBST(sequence[limit_index:-1])
            return left and right
        else:
            sub = self.VerifySquenceOfBST(sequence[:-1])
            return sub