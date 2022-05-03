from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        tmp = {}
        for i, n in enumerate(nums):
            cand = target - n
            if cand in tmp:
                return [i, tmp[cand]]
            tmp[n] = i
