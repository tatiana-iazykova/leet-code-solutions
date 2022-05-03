from typing import List


# Solution 1: blunt python solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


# Solution 2: iterative in-place solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):  # go over each letter and add the reverse one to it
            s[i] = s[i]+s[-i-1][0]

        for i in range(len(s)):  # go over again and just select the last one
            s[i] = s[i][1]