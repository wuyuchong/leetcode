#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if (target - num) in hashtable:
                return [hashtable[(target - num)], i]
            else:
                hashtable[num] = i
        return []
