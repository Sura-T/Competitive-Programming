class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hash_map = {}
        res = []
        for id,val in nums1:
            hash_map[id] = val

        for id,val in nums2:
            if id not in hash_map:
                hash_map[id] = val
            else:
                hash_map[id] += val

        for key,value in hash_map.items():
            res.append([key,value])
        
        res = sorted(res)

        return res
           