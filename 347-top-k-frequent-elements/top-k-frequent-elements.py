class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        sorted_nums = sorted(count.keys(), key=lambda num: count[num], reverse=True)
    
        return sorted_nums[:k]
