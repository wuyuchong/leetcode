#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sums = 0
        for i in s:
            sums += ord(i)
        sumt = 0
        for i in t:
            sumt += ord(i)
        return chr(sumt - sums)


