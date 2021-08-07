#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        whole = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(whole[i - 1][j - 1] + whole[i - 1][j])
            whole.append(row)
        return whole



