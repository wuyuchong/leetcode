#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_r = Counter(ransomNote)
        freq_m = Counter(magazine)
        for x in freq_r:
            if x not in freq_m or freq_r[x] > freq_m[x]:
                return False
        return True


