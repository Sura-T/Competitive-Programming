class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        max_long = 0
        while r <= len(s):
            if len(s[l:r]) == len(set(s[l:r])):
                curr_long = len(s[:r]) - l
                r += 1
            else:
                l += 1

            max_long = max(max_long,curr_long)
        return max_long

