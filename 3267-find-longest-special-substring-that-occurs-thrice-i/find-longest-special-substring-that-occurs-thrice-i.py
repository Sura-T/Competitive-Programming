class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        max_length = -1
        freq = defaultdict(int)

        for start in range(n):
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if len(set(substring)) == 1:
                    freq[substring] += 1

                    if freq[substring] >= 3:
                        max_length = max(max_length, len(substring))

        return max_length

        