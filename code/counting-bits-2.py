#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        highBits = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                highBits = i
            bits.append(bits[i - highBits] + 1)
        return bits
