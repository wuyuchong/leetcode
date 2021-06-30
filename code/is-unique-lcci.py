#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for char in astr:
            bit = ord(char) - ord('a')
            if mark & (1 << bit) == 0:
                mark |= (1 << bit) 
            else:
                return False
        return True
           



