class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the start and end of the list
        l, r = 0, len(height) - 1
        # Initialize the maximum area to 0
        maxArea = 0

        # Continue until the two pointers meet
        while l < r:
            # Calculate the current area as the product of the distance between the two pointers and the minimum height
            currArea = min(height[l], height[r]) * (r - l)
            # Update the maximum area if the current area is larger
            maxArea = max(maxArea, currArea)

            # Move the pointer at the shorter height towards the other pointer
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        # Return the maximum area
        return maxArea
