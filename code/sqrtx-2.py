#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 牛顿迭代

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        C = x 
        xi = x
        while True:
            x0 = xi
            xi = 0.5 * (xi + C / xi)
            if x0 - xi < 1e-7:
                return int(xi)



so = Solution()
print(so.mySqrt(1))
