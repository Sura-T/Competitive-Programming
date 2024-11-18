class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = []
        if k == 0:
            return [0] * n
        
        if k > 0:
            for i in range(n):
                sum_value = 0
                for j in range(1, k + 1):
                    sum_value += code[(i + j) % n]
                result.append(sum_value)
        
        else:
            for i in range(n):
                sum_value = 0
                for j in range(1, -k + 1):
                    sum_value += code[(i - j) % n]
                result.append(sum_value)
        
        return result
