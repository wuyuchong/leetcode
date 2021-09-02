#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []
        left, right = 0, 0
        while left < n and right < n:
            while right < (n - 1):
                if nums[right + 1] - nums[right] < 2:
                    right += 1
                else:
                    break
            res.append((nums[left], nums[right]))
            left = right + 1    
            right += 1
        def f(x):
            left, right = x
            if left == right:
                return str(left)
            else:
                return str(left) + '->' + str(right)
        return(list(map(f, res)))

            

