#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(' ')
        for i in x[::-1]:
            if i != '':
                return len(i)
        return 0


so = Solution()
print(so.lengthOfLastWord(''))
