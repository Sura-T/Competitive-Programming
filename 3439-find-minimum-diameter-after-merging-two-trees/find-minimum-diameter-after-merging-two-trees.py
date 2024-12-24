class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def tree_diameter(edges: List[List[int]], n: int) -> (int, int):
            def bfs(start: int) -> (int, int):
                dist = [-1] * n
                dist[start] = 0
                q = deque([start])
                farthest_node = start

                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if dist[neighbor] == -1:
                            dist[neighbor] = dist[node] + 1
                            q.append(neighbor)
                            farthest_node = neighbor

                return farthest_node, dist[farthest_node]

            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            start, _ = bfs(0)
            farthest_node, _ = bfs(start)
            _, diameter = bfs(farthest_node)

            return diameter

        n = len(edges1) + 1
        m = len(edges2) + 1

        diameter1 = tree_diameter(edges1, n)
        diameter2 = tree_diameter(edges2, m)

        return max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)
