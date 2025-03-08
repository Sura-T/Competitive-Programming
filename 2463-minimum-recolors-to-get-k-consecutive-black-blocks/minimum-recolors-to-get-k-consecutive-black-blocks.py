class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        cnt = 0
        l = 0
        min_val = float("inf")
        for r in range(n):
            if blocks[r] == "W":
                cnt += 1

            if r - l + 1 > k:
                if blocks[l] == "W":
                    cnt -= 1
                l += 1

            if r - l + 1 == k:
                min_val = min(min_val, cnt)
               
        return min_val
            

