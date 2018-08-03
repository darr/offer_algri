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
    #run:30ms memory:5720k
    def NumberOf1Between1AndN_Solution(self, n):
        k = 1
        if n < k:
            return 0
        count, m = 0, 1
        while m <= n:
            weight = n // m % 10
            count += (n // m) // 10 * m
            if weight == k:
                count += (n%m + 1)
            if weight > k:
                count += m
            m *= 10
        return count
    
    def NumberOf1Between1AndN_Solution2(self, n):
        k = 1
        if n < k:
            return 0
        count = 0
        base = 1
        r = n
        while r > 0:
            weight = r % 10
            r = r// 10
            count += r * base
            if weight == k:
                count += (n%base) + 1
            elif weight > k:
                count +=base
            base *= 10
        return count
    
    def NumberOf1Between1AndN_Solution3(self, n):
        k = 1
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 9 - k ) // 10 * m + (n // m % 10 == k) * (n % m + 1)
            m *= 10
        return ones