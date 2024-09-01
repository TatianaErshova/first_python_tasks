#!/usr/bin/env python3
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            print(i)
            print(nums)
            while (i < len(nums)-1) and (nums[i] == nums[i+1]):
                nums.pop(i+1)
                print(nums)
        return len(nums)




S = Solution()
S.removeDuplicates([1,2,3,3])