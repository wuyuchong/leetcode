#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set =  set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in num_set:
                return i

            
