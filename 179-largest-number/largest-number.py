class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #to sort in descending order
        def compare(x,y):
            return int(y+x) - int(x+y)

        #to change elements to string value
        nums = list(map(str,nums))
        #sort based on comparator key
        nums.sort(key = cmp_to_key(compare))
        result = ''.join(nums)

        return '0' if result[0] == '0' else result