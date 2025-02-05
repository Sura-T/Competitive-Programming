class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2 = Counter(s2)
        i = 0
        cnt = 0
        if count_s1 == count_s2:
            while i < len(s1):
                
                if s1[i] != s2[i]:
                    cnt += 1
                if cnt >2:
                    return False
                i += 1

        
            return True
        return False
