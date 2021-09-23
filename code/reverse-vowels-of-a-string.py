#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def reverseVowels(self, s: str) -> str:
        def judge(ch):
            return ch in 'aeiouAEIOU'
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if not judge(s[left]):
                left += 1
                continue
            if not judge(s[right]):
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

