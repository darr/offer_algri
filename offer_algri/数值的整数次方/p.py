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
    def Power(self, base, exponent):
        flag = 0
        if base == 0:
            return False
        if exponent == 0:
            return 1
        if exponent < 0:
            flag = 1
        ret = 1
        absExponent = abs(exponent)
        ret = self.pow(base,absExponent)
        if flag == 1:
            ret = 1/ret
        return ret

    def pow(self,X,N):
        if N == 0:
            return 1
        if N == 1:
            return X
        if N % 2 == 0:
            return self.pow(X*X,N/2)
        else:
            return self.pow(X*X,N/2) * X

    #run:21ms memory:5856k
    def Power2(self,base,exponent):
        flag = 0
        if base == 0:
            return False
        if exponent == 0:
            return 1
        if exponent < 0:
            flag = 1
        ret = 1
        absExponent = abs(exponent)
        for i in range(absExponent):
            ret *= base
        if flag == 1:
            ret = 1/ret
        return ret