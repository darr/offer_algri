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
    #run:22ms memory:5980k
    def FindPath(self, root, expectNumber):
        if None == root: return []
        return self.FindAPath(root,expectNumber,[],[])
     
    def FindAPath(self,root,expectNumber,path_list,lt):
        if None == root: return
        expectNumber = expectNumber - root.val
        lt.append(root.val)
        if expectNumber !=0:
            left_lt = list(lt)
            self.FindAPath(root.left,expectNumber,path_list,left_lt)
            right_lt = list(lt)
            self.FindAPath(root.right,expectNumber,path_list,right_lt)
        elif root.left == None and root.right == None:
            path_list.append(lt)
        return path_list

