class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to perform binary search
        def binSearch(nums, target, leftBias):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                m = l + (r - l) // 2  # Update midpoint in each iteration
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    i = m  # Record the index where target is found
                    # Adjust search range based on the bias
                    if leftBias:
                        r = m - 1  # Continue searching in the left half
                    else:
                        l = m + 1  # Continue searching in the right half
            return i

        # Use binSearch to find leftmost and rightmost positions
        left = binSearch(nums, target, True)
        right = binSearch(nums, target, False)
        return [left, right]
