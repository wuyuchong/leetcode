#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = set()
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            record.add(nums[i])
            if len(record) > k:
                record.remove(nums[i - k])
        return False
                
