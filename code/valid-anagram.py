#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        if len(s) != len(t):
            return False
        for index, value in enumerate(s):
            if value in hash_s:
                hash_s[value] += 1
            else:
                hash_s[value] = 1
        for index, value in enumerate(t):
            if value in hash_t:
                hash_t[value] += 1
            else:
                hash_t[value] = 1
        return hash_s == hash_t
