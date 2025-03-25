class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        merged_meetings = []
        for start, end in meetings:
            if not merged_meetings or merged_meetings[-1][1] < start:
                merged_meetings.append([start, end])
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], end)

        occupied_days = 0
        for start, end in merged_meetings:
            occupied_days += end - start + 1

        available_days = days - occupied_days
        return available_days
