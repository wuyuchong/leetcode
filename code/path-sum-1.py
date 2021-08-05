#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que = collections.deque([(root, root.val)])
        while que:
            node, cumsum = que.popleft()
            if not node.left and not node.right:
                if cumsum == sum:
                    return True
            if node.left:
                que.append((node.left, cumsum + node.left.val))
            if node.right:
                que.append((node.right, cumsum + node.right.val))
        return False
