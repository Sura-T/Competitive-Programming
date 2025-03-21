class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx):
            if idx == n:
                permutations.append(current_permutation[:])
                return

            for j in range(n):
                if not visited[j]:
                    visited[j] = True
                    current_permutation[idx] = nums[j]
                    backtrack(idx + 1)

                    visited[j] = False

        n = len(nums)
        visited = [False] * n
        current_permutation = [0] * n
        permutations = []
        backtrack(0)

        return permutations