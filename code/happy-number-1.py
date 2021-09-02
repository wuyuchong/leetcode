#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total = 0
            while n > 0:
                remain = n % 10
                n = n // 10
                total += remain ** 2
            return total



        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

