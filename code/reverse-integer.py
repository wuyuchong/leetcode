#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def reverse(self, x: int) -> int:

        INT_MAX = 2**31

        if x < 0:
            flag = True
            x = -x
        elif x > 0:
            flag = False
        else:
            return 0

        outcome = 0
        while x != 0:
            digit = x % 10
            x = x // 10
            if outcome > (INT_MAX // 10):
                return 0
            else:
                outcome = outcome * 10 + digit
        if flag == True:
            return -outcome
        else:
            return outcome


s = Solution()
print(s.reverse(-123))
            

