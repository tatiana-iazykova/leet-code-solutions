# Solution 1: convert to a string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# Solution 2: staying with int
# Break down the number to its digits and check
class Solution:
    def isPalindrome(self, x: int) -> bool:

        return self.f(x)

    def f(self, n):
        l = []
        const = 1_000_000_000  # 2**31-1  --- our largest number

        if n < 0:  # corner cases
            return False

        if n < 10:  # corner cases
            return True

        if n % 10 == 0:  # corner cases
            return False

        if n > const:
            while n != 0:
                q, n, const = self.recursive_strip(n, const)
                l.append(q)

        else:
            const = 10
            while const < n:
                const *= const

            while n > 0:
                q, n, const = self.recursive_strip(n, const)
                l.append(int(q)) # sometimes it may be a float

        f = l[0]
        while f == 0:
            l = l[1:]
            f = l[0]

        if l[-1] == 0:
            _ = l.pop()

        if l[0] == 0:
            l = l[1:]
        return l == l[::-1]

    @staticmethod
    def recursive_strip(n, num):
        q = n // num
        n -= q * num

        return q, n, num / 10
