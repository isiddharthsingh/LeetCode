class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        minLens = {}  # Dictionary to store minimum side lengths for each character
        secondMin = float("inf")  # Initialize the second minimum side length

        for point, char in zip(points, s):
            # Calculate the size (maximum absolute coordinate value) of the point
            size = max(abs(point[0]), abs(point[1]))

            if char not in minLens:
                minLens[char] = size
            elif size < minLens[char]:
                # Update the second minimum side length if a smaller one is found
                secondMin = min(minLens[char], secondMin)
                minLens[char] = size
            else:
                # Update the second minimum side length
                secondMin = min(secondMin, size)

        count = 0
        for length in minLens.values():
            if length < secondMin:
                count += 1  # Count characters with the second minimum side length

        return count
