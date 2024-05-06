"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sort the start times and end times separately
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count, s, e = 0, 0, 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                # If the current meeting starts before the previous meeting ends,
                # allocate a new room (increment count)
                s += 1
                count += 1
            else:
                # Otherwise, release a room (decrement count)
                e += 1
                count -= 1
            
            # Update the maximum number of rooms needed
            res = max(res, count)

        return res
