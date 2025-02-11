class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = Counter(s)
        res = []
        for key,value in s_count.items():
            res.append((value,key))

        string = ''
        res.sort(reverse=True)
        for key,value in res:
            string += (value * key)
        return string

            
        