#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = {}
        for num in nums:
            if not hashtable.get(num):
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        
        max_value = 0
        for key, value in hashtable.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key

