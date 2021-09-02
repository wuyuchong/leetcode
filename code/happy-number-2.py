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

        left = n
        right = get_next(n)
        while right != 1:
            if left == right:
                return False
            left = get_next(left)
            right = get_next(get_next(right))
        return True

        


