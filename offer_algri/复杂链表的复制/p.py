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


# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    #run:32ms memory:5728k
    def Clone(self, pHead):
        if pHead == None:
            return 
        head = pHead
        while head:
            nd = RandomListNode(0)
            nd.label = head.label
            nd.next = head.next
            head.next = nd
            head = nd.next
            
        head = pHead
        while head:
            nd = head.next
            if head.random != None:
                nd.random = head.random.next
            head = nd.next
        
        head = pHead
        nHead =  head.next
        nNode = head.next
        head.next = nNode.next
        head = head.next
        while head :
            nNode.next = head.next
            nNode = nNode.next
            head.next = nNode.next
            head = head.next
        return nHead
