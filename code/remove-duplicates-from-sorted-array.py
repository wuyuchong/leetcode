#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        num = None
        for fast in range(len(nums)):
            if nums[fast] != num:
                num = nums[fast]
                nums[slow] = num
                slow += 1
        return slow



