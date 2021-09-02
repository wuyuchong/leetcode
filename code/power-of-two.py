#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1) == 0)
