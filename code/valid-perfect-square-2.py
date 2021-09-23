#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num 


