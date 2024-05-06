class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # Initialize an empty list to store the merged intervals

        for i in range(len(intervals)):
            # If the end of the new interval is before the start of the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)  # Add the new interval to the result
                return res + intervals[i:]  # Append the remaining intervals
            # If the start of the new interval is after the end of the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])  # Add the current interval to the result
            else:
                # Merge overlapping intervals by updating the new interval
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]

        res.append(newInterval)  # Add the final merged interval
        return res
