from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # easy case
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        # otherwise
        else:
            digits[-1] = 0
            if len(digits) == 1:  # we have a 9
                digits.insert(0, 1)
                return digits

            for i in range(len(digits) - 2, -1, -1):
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                elif digits[i] == 9 and i != 0:
                    digits[i] = 0
                else:
                    digits[i] = 0
                    digits.insert(0, 1)
                    return digits
