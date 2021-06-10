#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        outcome = 0
        for i, c in enumerate(s):
            value = self.SYMBOL_VALUES[c]
            if i == (len(s) - 1):
                outcome += value
            elif self.SYMBOL_VALUES[c] >= self.SYMBOL_VALUES[s[i + 1]]:
                outcome += value
            else:
                outcome -= value
        return outcome

so = Solution()
print(so.romanToInt('MCMXCIV'))

