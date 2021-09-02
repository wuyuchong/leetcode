#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans <<= 1
            ans = ans | (n & 1)
            n >>= 1
        return ans

