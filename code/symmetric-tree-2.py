#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or not (root.left or root.right):
            return True
        q = collections.deque([root.left, root.right])
        while q:
            left = q.popleft()
            right = q.popleft()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False

            q.append(left.left)
            q.append(right.right)

            q.append(left.right)
            q.append(right.left)

        return True
                

        
