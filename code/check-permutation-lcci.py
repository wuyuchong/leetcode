#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        result = 0
        for i in range(len(s1)):
            result += 1 << (ord(s1[i]) - ord('a')) 
            result -= 1 << (ord(s2[i]) - ord('a')) 
        return result == 0

