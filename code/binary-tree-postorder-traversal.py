#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(False, root)]
        out = []
        while stack:
            flag, node = stack.pop()
            if node is None:
                continue
            elif flag:
                out.append(node.val)
            else:
                stack.append((True, node))
                stack.append((False, node.right))
                stack.append((False, node.left))
        return out

