class Solution:
    def romanToInt(self, s: str) -> int:

        ref = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        if s in ref:
            return ref[s]

        other = []

        for i in range(len(s) - 1):
            double = s[i] + s[i + 1]
            if double in ref:
                other.append(double)

        cur = 0

        for o in other:
            s = s.replace(o, '')
            cur += ref[o]

        for c in s:
            cur += ref[c]

        return cur
