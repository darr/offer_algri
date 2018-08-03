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
    def EntryNodeOfLoop(self, pHead):
        if pHead == None:
            return None
        pSlow = pHead.next
        if pSlow == None:
            return None
        pFast = pSlow.next
        while pFast:
            if pSlow == pFast:
                break
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next
        NodeLoop = 1
        flagNode = pSlow
        while flagNode.next != pSlow:
            NodeLoop += 1
            flagNode = flagNode.next
            
        pFirst = pHead
        for i in range(NodeLoop):
            pFirst = pFirst.next
        pSecond = pHead
        while pFirst != pSecond:
            pFirst = pFirst.next
            pSecond = pSecond.next
        return pFirst