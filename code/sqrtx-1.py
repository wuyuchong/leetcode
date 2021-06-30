#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 二分法

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        left = 0
        right = x
        mid = (left + right) // 2
        while True:
            if mid ** 2 == x or (mid ** 2 < x and (mid + 1) ** 2 > x):
                return mid
            elif mid ** 2 > x:
                right = mid
                mid = (left + right) // 2
            elif mid ** 2 < x:
                left = mid
                mid = (left + right) // 2
            else:
                print('error')

so = Solution()
print(so.mySqrt(1))
