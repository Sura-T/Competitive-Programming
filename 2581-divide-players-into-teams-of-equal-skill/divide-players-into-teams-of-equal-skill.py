class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        res = []
        while l < r:
            res.append((skill[l],skill[r]))
            l += 1
            r -= 1
        chemistry = 0
        sum1 = skill[l] + skill[r]
        for key,value in res:
            if key + value != sum1:
                return -1
            elif key + value == sum1:
                chemistry += (key * value)
        
        return chemistry
