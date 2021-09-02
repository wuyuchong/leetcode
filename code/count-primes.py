#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def countPrimes(self, n: int) -> int:
        judge = [True] * (n - 1)
        count = 0
        for i in range(2, n):
            if judge[i - 1]:
                count += 1
                j = i * 2
                while j < n:
                    judge[j - 1] = False
                    j += i
        return count

