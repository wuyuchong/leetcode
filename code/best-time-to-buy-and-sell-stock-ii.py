#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        earning = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                earning += prices[i] - prices[i - 1]
        return earning
