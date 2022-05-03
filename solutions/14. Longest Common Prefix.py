from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs[0]):
            return ''
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0]), 0, -1):
            s = strs[0][:i]
            if all([x.startswith(s) for x in strs]):
                return s
        return ''
