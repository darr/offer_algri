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
    #run:24ms memory:5732k
    def getlt(self,pRoot,lt,k):
        if pRoot == None:
            return 
        self.getlt(pRoot.left,lt,k)
        if len(lt)<k+1:
            lt.append(pRoot)
            self.getlt(pRoot.right,lt,k)
            
    def KthNode(self, pRoot, k):
        if pRoot == None or k < 1:
            return None
        lt = []
        self.getlt(pRoot,lt,k)
        if len(lt) < k:
            return None
        return lt[k-1]