#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            if (counter := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                #  if m[num] == 0:
                    #  m.pop(num)
                    
        return intersection
