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
    def TreeMaxDepth(self, pRoot):
        if pRoot == None:
            return 0
        return max(self.TreeMaxDepth(pRoot.left),self.TreeMaxDepth(pRoot.right)) + 1

    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.TreeMaxDepth(pRoot.right) - self.TreeMaxDepth(pRoot.left)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
