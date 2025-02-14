class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                s_left = s[:left] + s[left+1:]
                r_left = s[:right] + s[right+1:]
            
                if s_left[::-1] == s_left or r_left[::-1] == r_left:
                    return True
                else:
                    return False

            left += 1
            right -= 1

        return True
        

            
        