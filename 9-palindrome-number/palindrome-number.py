class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        else:
            y = 0
            while y < x:
                y = y * 10 + x % 10
                x //= 10
        return x == y or x == y // 10