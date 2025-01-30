class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        else:
            y = 0
            cx = x
            while x != 0:
                y = y * 10 + x % 10
                x //= 10
        return cx == y