#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        flag = True
        for i in range(len(s) - 1, -1, -1):
            if flag and s[i] != ' ':
                length += 1
                flag = False
            elif flag == False and s[i] != ' ':
                length += 1
            elif flag == False and s[i] == ' ':
                return length
            else:
                continue
        return length


so = Solution()
print(so.lengthOfLastWord('f '))
