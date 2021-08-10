#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low = i + 1
            high = n - 1
            while low <= high and low < n and high < n: 
                mid = (low + high) // 2
                if numbers[mid] + numbers[i] == target:
                    return [i + 1, mid + 1]
                elif numbers[mid] + numbers[i] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return False


