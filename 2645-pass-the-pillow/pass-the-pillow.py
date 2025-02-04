class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cnt_n = 1
        dir=1
        for _ in range(time):
            cnt_n+=dir
            if cnt_n==n:
                dir=-1
            elif cnt_n==1:
                dir=1
            

        return cnt_n 
       