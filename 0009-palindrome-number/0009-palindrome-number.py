class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse = x[::-1]
        return x == reverse
        