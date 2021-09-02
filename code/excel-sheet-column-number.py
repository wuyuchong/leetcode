#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = list(columnTitle)
        l = l[::-1]
        n = 0
        ans = 0
        for char in l:
            ans += (ord(char) - ord("A") + 1) * (26 ** n)
            n += 1
        return ans

