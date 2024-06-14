class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize two pointers at the left and right ends of the array
        l, r = 0, len(height) - 1
        # Initialize variables to track the maximum height on the left and right
        maxLeft, maxRight = height[l], height[r]
        # Initialize the result variable to store the trapped water amount
        res = 0

        # While the left pointer is less than the right pointer
        while l < r:
            # If the maximum height on the left is less than the maximum height on the right
            if maxLeft < maxRight:
                # Move the left pointer to the right
                l += 1
                # Update the maximum height on the left
                maxLeft = max(maxLeft, height[l])
                # Add the trapped water between the current height and the maximum height on the left
                res += maxLeft - height[l]
            else:
                # Otherwise, move the right pointer to the left
                r -= 1
                # Update the maximum height on the right
                maxRight = max(maxRight, height[r])
                # Add the trapped water between the current height and the maximum height on the right
                res += maxRight - height[r]

        # Return the total trapped water amount
        return res
