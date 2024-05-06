class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # Sort intervals based on the start value

        res = 0  # Initialize a counter for overlapping intervals
        prevEnd = intervals[0][1]  # Initialize the end value of the first interval

        for start, end in intervals[1:]:
            if start >= prevEnd:
                # If the current interval does not overlap with the previous one,
                # update the end value to the current interval's end
                prevEnd = end
            else:
                # Otherwise, increment the counter and update the end value to the minimum
                # of the current interval's end and the previous interval's end
                res += 1
                prevEnd = min(end, prevEnd)
        
        return res
