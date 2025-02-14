class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l = 0
        r = len(people) - 1
        cnt = 0
        while l <=r:
            if people[l] + people[r] <= limit:
                cnt += 1
                l += 1
                r -= 1
            elif people[r] + people[l] > limit:
                cnt += 1
                l += 1

        return cnt
                

                
                
            
             
