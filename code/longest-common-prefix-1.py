#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(1, len(strs)):
            common = self.compare(strs[i], common)
        return common

    def compare(self, str1, str2):
        final_index = -1
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                final_index = i
            else:
                break
        return str1[:(final_index + 1)]



so = Solution()
print(so.longestCommonPrefix(['long', 'longest']))
            



