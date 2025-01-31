class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        #always to increase num by 1 and decrease x by 1
        for _ in range(t):
            num += 1
            
        x = num + t
        return x