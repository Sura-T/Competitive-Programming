class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum1 = 0
        for account in accounts:
            if sum(account) > sum1:
                sum1 = sum(account)

        return sum1