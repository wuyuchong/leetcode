#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (right + left) // 2

        if nums[left] > target:
            return left
        if nums[right] == target:
            return right
        if nums[right] < target:
            return right + 1

        while True:
            if nums[mid] == target:
                return mid
            elif mid == left:
                return mid + 1
            elif nums[mid] < target:
                left = mid
                mid = (right + left) // 2 
            elif nums[mid] > target:
                right = mid
                mid = (right + left) // 2
            else:
                print('error')

so = Solution()
print(so.searchInsert([1,2,4], 3))

