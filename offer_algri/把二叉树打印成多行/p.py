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
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        lt = []
        self.printTree(lt,pRoot,0)
        return lt
        
    def printTree(self,lt,pRoot,deep):
        if pRoot == None:
            return 
        while len(lt) < deep+1:
            lt.append([])
        l = lt[deep]
        l.append(pRoot.val)
        self.printTree(lt,pRoot.left,deep+1)
        self.printTree(lt,pRoot.right,deep+1)