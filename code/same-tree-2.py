#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        q1 = collections.deque([p])
        q2 = collections.deque([q])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1.val != node2.val:
                return False
            if (not node1.left) ^ (not node2.left):
                return False
            if (not node1.right) ^ (not node2.right):
                return False
            if node1.left:
                q1.append(node1.left)
            if node1.right:
                q1.append(node1.right)
            if node2.left:
                q2.append(node2.left)
            if node2.right:
                q2.append(node2.right)

        return not q1 and not q2

