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


# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    #run:35ms memory:5724k
    def GetNext(self, pNode):
        if pNode == None:
            return 
        pNext = None
        if pNode.right != None:
            pRight = pNode.right
            while pRight.left !=None:
                pRight = pRight.left
            pNext = pRight
        elif pNode.next != None:
            pCurrent = pNode
            pParent = pNode.next
            while pParent != None and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pParent.next
            pNext = pParent
        return pNext