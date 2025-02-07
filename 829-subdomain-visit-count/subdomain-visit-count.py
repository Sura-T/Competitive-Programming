class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        my_dict = {}

        for path in cpdomains:
            index = path.index(" ")
            num = path[:index+1]

            my_dict[path[index+1:]] = my_dict.get(path[index+1:],0) + int(num)
            domain = path[index+1:]  
            
            for i in range(len(domain)):
                if domain[i] == ".":
                    my_dict[domain[i+1:]] = my_dict.get(domain[i+1:],0) + int(num)
        
        for key,value in my_dict.items():
            elem = str(value) + " " + key
            
            res.append(elem)

        return res
        