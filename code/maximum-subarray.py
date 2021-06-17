#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        hold = 0
        maximum = nums[0]
        for i in nums:
            maximum = max(hold + i, maximum)
            if hold + i > 0:
                hold += i 
            else:
                hold = 0
        return maximum

