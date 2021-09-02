#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for n in nums:
            if n not in record:
                record.add(n)
            else:
                return True
        return False
