#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def compare(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
        
