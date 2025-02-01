class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split() #change to list
        return len(s[len(s)-1])
