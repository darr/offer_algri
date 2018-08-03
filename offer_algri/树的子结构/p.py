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
    #run:27ms memory:5612k
    def HasSubtree(self, pRoot1, pRoot2):
        ret = False
        if pRoot2 is None or pRoot1 is None:
            return ret 
        if pRoot1.val == pRoot2.val:
            ret  = self.doesTree1HasTree2(pRoot1,pRoot2)
        if ret == False:
            ret = self.HasSubtree(pRoot1.left,pRoot2)
        if ret == False:
            ret = self.HasSubtree(pRoot1.right,pRoot2)
        return  ret 
    
    def doesTree1HasTree2(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.doesTree1HasTree2(pRoot1.left,pRoot2.left) and self.doesTree1HasTree2(pRoot1.right,pRoot2.right)