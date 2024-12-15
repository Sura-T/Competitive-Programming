class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(passi, totali):
            return (passi + 1) / (totali + 1) - passi / totali
    
        heap = []
        for passi, totali in classes:
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))
    
        for _ in range(extraStudents):
            max_gain, passi, totali = heapq.heappop(heap)
            passi += 1
            totali += 1
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))
        total_ratio = 0
        for _, passi, totali in heap:
            total_ratio += passi / totali
    
        return total_ratio / len(classes)
