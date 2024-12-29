class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words), len(words[0]) 
        t_len = len(target)

        char_count = [Counter() for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                char_count[i][char] += 1

        dp = [0] * (t_len + 1)
        dp[0] = 1

        for col in range(n):
            for j in range(t_len - 1, -1, -1):
                char = target[j]
                if char in char_count[col]:
                    dp[j + 1] += dp[j] * char_count[col][char]
                    dp[j + 1] %= MOD

        return dp[t_len]
