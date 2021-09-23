#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            x = (left + right) // 2
            if x * x == num:
                return True
            elif (x + 1) * (x + 1) == num:
                return True
            elif x * x > num:
                right = x - 1
            else:
                left = x + 1
        return False

