#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def countBits(self, n: int) -> List[int]:
        def countone(x):
            i = 0
            while x > 0:
                x = x & (x - 1)
                i += 1
            return i
        
        return [countone(x) for x in range(n + 1)]
