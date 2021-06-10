#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if (x < 0) or (x % 10 == 0):
            return False
        r = 0
        while x > r:
            r = r * 10 + x % 10
            x = x // 10
        return (x == r) or (x == r // 10)

so = Solution()
print(so.isPalindrome(14141))
        

