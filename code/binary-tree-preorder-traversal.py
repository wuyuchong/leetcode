#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(False, root)]
        out = []
        while stack:
            flag, node = stack.pop()
            if node:
                if flag:
                    out.append(node.val)
                else:
                    stack.append((False, node.right))
                    stack.append((False, node.left))
                    stack.append((True, node))
        return out


