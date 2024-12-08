class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        
        max_values = [0] * len(events)
        max_value = 0
        
        for i in range(len(events)):
            max_value = max(max_value, events[i][2])
            max_values[i] = max_value
        
        end_times = [event[1] for event in events]
        
        result = 0
        
        for i in range(len(events)):
            current_value = events[i][2]
            
            idx = bisect.bisect_right(end_times, events[i][0] - 1) - 1
            
            if idx >= 0:
                result = max(result, current_value + max_values[idx])
            else:
                result = max(result, current_value)
        
        return result
