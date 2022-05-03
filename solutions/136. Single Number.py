from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        if nums[1] != nums[0]:
            return nums[0]

        for i in range(1, len(nums)):
            if i + 1 == len(nums):
                if nums[i - 1] != nums[i]:
                    return nums[i]
            if nums[i - 1] != nums[i] and nums[i] != nums[i + 1]:
                return nums[i]
