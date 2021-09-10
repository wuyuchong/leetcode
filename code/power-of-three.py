#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: 
            return False
        else:   
            e = log10(n) / log10(3)
            return e == floor(e)
