class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        i = 0
        while i < len(s):
            while i < len(s)-1 and s.count(s[i]) != s.count(s[i+1]):
                return False
            i += 1
        return True