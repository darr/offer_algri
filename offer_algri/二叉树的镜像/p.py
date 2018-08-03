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
    #run:22ms memory:5732k
    def Mirror(self,root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.Mirror(root.left)
        self.Mirror(root.right)
                
    #run:31ms memory:5716k
    def Mirror2(self, root):
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.Mirror(root.right)
        self.Mirror(root.left)