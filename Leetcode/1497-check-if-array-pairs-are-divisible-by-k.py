class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_count = Counter(x % k for x in arr)
        if remainder_count[0] % 2 != 0:
            return False
        for remainder in range(1, k):
            if remainder_count[remainder] != remainder_count[k - remainder]:
                return False
        return True
        