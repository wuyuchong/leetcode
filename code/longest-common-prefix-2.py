#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for column in range(len(strs[0])):
            if any(column == len(strs[row]) or (strs[0][column] != strs[row][column]) for row in range(1, len(strs))):
                return strs[0][:column]
        return strs[0]

so = Solution()
print(so.longestCommonPrefix(['long', 'longest']))
