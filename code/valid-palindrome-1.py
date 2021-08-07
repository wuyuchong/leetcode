#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = ''.join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]
