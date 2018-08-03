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
    def Print(self,root):
        if not root:
            return []
        levels,result,leftToRight = [root],[],True
        while levels:
            curValues,nextLevel = [],[]
            for node in levels:
                curValues.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if not leftToRight:
                curValues.reverse()
            if curValues:
                result.append(curValues)
            levels = nextLevel
            leftToRight = not leftToRight
        return result