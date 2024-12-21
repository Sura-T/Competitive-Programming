class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        self.max_components = 0
        def dfs(node, parent):
            subtree_sum = values[node]
            
            for neighbor in tree[node]:
                if neighbor != parent:
                    subtree_sum += dfs(neighbor, node)
            
            if subtree_sum % k == 0:
                self.max_components += 1
                return 0 
            
            return subtree_sum  
        dfs(0, -1)
        
        return self.max_components
