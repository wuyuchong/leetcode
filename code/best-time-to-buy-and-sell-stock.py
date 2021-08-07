#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 100000
        max_earning = 0
        for price in prices:
            minimum = min(price, minimum)
            earning = price - minimum
            max_earning = max(earning, max_earning)
        return max_earning



