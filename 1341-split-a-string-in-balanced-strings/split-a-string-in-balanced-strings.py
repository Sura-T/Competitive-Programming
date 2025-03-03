class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        cur = 0
        for char in s:
            if char == "L":
                cur += 1
            else:
                cur -= 1
            
            if cur == 0:
                ans += 1

        return ans