#!/usr/bin/env python3
from typing import List
class Solution:
    def shorteststring(self,strs):
            i = 0
            length = len(strs[0])
            shortest = strs[0]
            for i in range(1,len(strs)):
                if len(strs[i]) < length:
                    length = len(strs[i])
                    shortest = strs[i]
            return(shortest)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        int_result = ' '
        shortest = self.shorteststring(strs)
        for i in range(len(shortest)):
            if int_result == '':
                 break
            int_result = ''
            for j in range(len(strs)):
                if shortest[i] == strs[j][i]:
                    int_result = shortest[i]
                    #print(int_result)
                else:
                     int_result = ''
                     break
            result += int_result
            print(result)
        return(result)
        # if shortest[]
S = Solution()
S.shorteststring(["flower", "flo", "flssjs"])
S.longestCommonPrefix(["flower", "flo", "flssjs"])
#print(S.longestCommonPrefix(["flower", "flo", "flssjs"]))
#print(S.longestCommonPrefix(["flssjs", "flo", "flower"]))
#print(S.shorteststring(["flower", "flo", "flssjs"]))
#assert(S.shorteststring(["flower", "flo", "flssjs"]) == "flo")
#assert(S.shorteststring(["flo", "flower", "flssjs"]) == "flo")
#assert(S.longestCommonPrefix(["flssjs", "flo", "flower"]) == 'f', 'hhhhhhh')
assert(S.longestCommonPrefix(['aba','aca','ada']) == 'a')