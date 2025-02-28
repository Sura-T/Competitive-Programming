class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        index_k = nums.index(k)
        balance_counter = Counter()
        cnt = 1
        balance = 0

        for num in nums[index_k+1:]:
            if num > k:
                balance += 1
            else:
                balance -= 1
            if balance >= 0 and balance <= 1:
                cnt += 1
            balance_counter[balance] += 1

        balance = 0
        for j in range(index_k - 1, -1, -1):
            if nums[j] > k:
                balance += 1
            else:
                balance -= 1
            if balance >= 0 and balance <= 1:
                cnt += 1
            cnt += balance_counter[-balance] + balance_counter[-balance + 1]

        return cnt
            

