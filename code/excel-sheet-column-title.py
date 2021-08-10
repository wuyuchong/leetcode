#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            x = (columnNumber - 1) % 26
            ans.append(chr(x + ord('A')))
            columnNumber = (columnNumber - x - 1) // 26
        return ''.join(ans[::-1])



