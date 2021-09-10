#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = (left + right) // 2
        while left != mid:
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
            mid = (left + right) // 2
        if isBadVersion(mid):
            return mid
        else:
            return mid + 1
