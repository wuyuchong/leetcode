#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        p1 = 0
        p2 = 0
        while p1 <= m and p2 <= n:
            if p1 == m:
                nums += nums2[p2:n]
                break
            elif p2 == n:
                nums += nums1[p1:m]
                break
            elif nums1[p1] > nums2[p2]:
                nums.append(nums2[p2])
                p2 += 1
            else:
                nums.append(nums1[p1])
                p1 += 1

        nums1[:] = nums





