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
    def Serialize(self,root):
        if root == None:
            return "#"
        stack = []
        serializeStr = ''
        while root or stack:
            while root:
                serializeStr +=str(root.val) + ','
                stack.append(root)
                root=root.left
            serializeStr += "#,"
            root = stack.pop()
            root = root.right
        serializeStr = serializeStr[:-1]
        return serializeStr
    
    def Deserialize(self, s):
        serialize = s.split(',')
        tree,sp = self.deserialize(serialize,0)
        return tree
    
    def deserialize(self,s,sp):
        if sp >=len(s) or s[sp] == '#':
            return None, sp+1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left,sp = self.deserialize(s,sp)
        node.right,sp = self.deserialize(s,sp)
        return node,sp