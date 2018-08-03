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
    #run:25ms memory:5856k
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        pMergedHead = None
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1, pHead2.next)
        return pMergedHead

    #run:30ms memory:5712k
    def Merge2(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        pMergeHead = None
        pMergeNode = None
        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pHead1 = pHead1.next
        else:
            pMergeHead = pHead2
            pHead2 = pHead2.next
        pMergeNode = pMergeHead
        while pHead1 is not None or pHead2 is not None:
            if pHead1 is None:
                pMergeNode.next = pHead2
                break
            if pHead2 is None:
                pMergeNode.next = pHead1
                break
            if pHead1 is not None and pHead2 is not None:
                if pHead1.val < pHead2.val:
                    pMergeNode.next = pHead1
                    pMergeNode = pHead1
                    pHead1 = pHead1.next
                else:
                    pMergeNode.next = pHead2
                    pMergeNode = pHead2
                    pHead2 = pHead2.next
        return pMergeHead