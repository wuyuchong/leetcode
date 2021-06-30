#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        fx_1 = 2
        fx_2 = 1 
        for i in range(3, n + 1):
            fx = fx_1 + fx_2
            fx_2 = fx_1
            fx_1 = fx
        return fx

so = Solution()
print(so.climbStairs(5))


