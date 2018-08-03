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

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self,pRootOfTree):
        if pRootOfTree == None:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        left = pRootOfTree.left
        if left:
            self.Convert(left)
            while left.right:
                left = left.right
            pRootOfTree.left,left.right = left,pRootOfTree
            
        right = pRootOfTree.right
        if right:
            self.Convert(right)
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right,pRootOfTree
            
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree