"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals)-1):
            start = intervals[i]
            end = intervals[i+1]
            if start.end > end.start:
                return False
        return True