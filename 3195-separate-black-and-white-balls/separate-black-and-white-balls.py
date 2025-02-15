class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        cnt = 0
        for r in range(len(s)-1,-1,-1):
            if s[r] == '0':
                cnt += 1
            elif s[r] == '1':
                ans += cnt

        return ans


            
            