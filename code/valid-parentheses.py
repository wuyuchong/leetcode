#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        if len(s) % 2 == 1 or len(s) == 0:
            return False

        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0

so = Solution()
print(so.isValid('[()]'))


