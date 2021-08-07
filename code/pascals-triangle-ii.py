#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def getRow(self, rowIndex):
        outcome = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                outcome[j] += outcome[j - 1]
        return outcome

