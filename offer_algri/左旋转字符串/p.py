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
    #run:25ms memory:5732k
    def LeftRotateString(self, s, n):
        lt = list(s)
        ns = lt[:n]
        lt = lt[n:]
        lt.extend(ns)
        return "".join(lt)