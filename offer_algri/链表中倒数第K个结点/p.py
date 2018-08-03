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


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #run:33ms memory:5728k
    def FindKthToTail(self, head, k):
        if k<=0 or head == None:
            return None
        p = head
        ret = head
        for i in range(k):
            if p:p = p.next
            else:return None
        while(p):
            p = p.next
            ret = ret.next
        return ret
        
    #run:22ms memory:5852k
    def FindKthToTail2(self, head, k):
        if k<=0 or head == None:
            return None
        else:
            count = 0
            p = head
            ret = head
            while p!=None:
                count = count + 1
                if count > k:
                    ret=ret.next
                p = p.next
            if count < k:
                ret = None
            return ret