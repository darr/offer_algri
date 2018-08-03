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
    def maxInWindows(self, num, size):
        if not num or size <= 0:
            return []
        deque = []
        last_max_index = -1
        if len(num) >= size:
            for i in range(len(num)-size+1):
                if last_max_index >= i:
                    v = num[i+size-1]
                    if v >= num[last_max_index]:
                         last_max_index = i+size-1
                    deque.append(num[last_max_index])
                else:
                    max_value = num[i]
                    for j in range(1,size):
                        v = num[i+j]
                        if v > max_value:
                            max_value = v
                            last_max_index = i+j
                    deque.append(max_value)
        return deque
    
    def maxInWindows2(self, num, size):
        if not num or size <= 0:
            return []
        deque = []
        if len(num) >= size:
            for i in range(len(num)-size+1):
                max_value = num[i]
                for j in range(1,size):
                    v = num[i+j]
                    if v > max_value:
                        max_value = v
                        last_max_index = i+j
                deque.append(max_value)
        return deque