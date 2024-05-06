"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)  # Sort intervals based on the start value
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                # If the end time of the previous interval overlaps with the start time of the current interval,
                # return False (meeting conflict)
                return False

        # If no conflicts found, return True (all meetings can be attended)
        return True
