class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start value
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]  # Initialize the output list with the first interval

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]  # Get the end value of the last interval in the output

            if start <= lastEnd:
                # If the current interval overlaps with the last interval in the output,
                # merge them by updating the end value
                output[-1][1] = max(lastEnd, end)
            else:
                # Otherwise, add the current interval to the output
                output.append([start, end])

        return output
