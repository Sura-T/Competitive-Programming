class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = Counter(s1)
        m = len(s1)
        l = 0
        for r in range(m,len(s2)+1):
            if Counter(s2[l:r]) == freq_s1:
                return True
            l += 1

        return False

