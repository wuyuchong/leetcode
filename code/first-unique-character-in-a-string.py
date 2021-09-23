#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = collections.Counter(s)
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i 
        return -1
