class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        count = 0
        for i in range(n):
            if 3 ** i == n:
                return True
            if 3 ** i > n:
                return False
        