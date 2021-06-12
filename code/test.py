#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

result = ListNode(0)
p1 = result
p2 = result
p1.next = ListNode(1)
p2 = p2.next
print(p1.val)
print(p2.val)
