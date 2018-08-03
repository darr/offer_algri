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


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #run:35ms memory:5864k
    def printListFromTailToHead(self, listNode):
        ret = []
        if listNode is None:
            return ret
        while listNode.next is not None:
            ret.append(listNode.val)
            listNode = listNode.next
        ret.append(listNode.val)
        ret.reverse()
        return ret