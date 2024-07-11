class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points in ascending order
        points.sort(key=lambda x:x[1])

        # Initialize the result as the total number of points
        res = len(points)
        # Keep track of the previous interval
        prevInterval = points[0]

        # Iterate over the points starting from the second one
        for i in range(1, len(points)):
            # Get the current interval
            currInterval = points[i]
            # If the start of the current interval is less than the end of the previous interval
            if currInterval[0] <= prevInterval[1]:
                # Decrease the result by 1 because we can shoot an arrow that covers both intervals
                res -= 1
                # Update the previous interval to be the intersection of the two intervals
                prevInterval = [currInterval[0], min(currInterval[1], prevInterval[1])]
            else:
                # If the current interval does not intersect with the previous one, update the previous interval
                prevInterval = currInterval
        # Return the minimum number of arrows needed
        return res
