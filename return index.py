#!/usr/bin/env python3
from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
S = Solution()
assert(S.strStr('haystack', 'g') == -1)
assert(S.strStr('haystack', 'a') == 1)
assert(S.strStr('haystack', 'sta') == 3)