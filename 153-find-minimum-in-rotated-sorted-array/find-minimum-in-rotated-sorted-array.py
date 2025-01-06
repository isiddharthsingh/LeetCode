class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize two pointers: l (left) at the start and r (right) at the end of the array
        l, r = 0, len(nums) - 1
        
        # Initialize the result with the first element of the array
        res = nums[0]

        # Perform a binary search while l <= r
        while l <= r:
            # If the subarray is already sorted, the smallest element is nums[l]
            if nums[l] <= nums[r]:
                res = min(res, nums[l])  # Update res with the smaller of the current res and nums[l]
                break  # Exit the loop since the minimum has been found
            else:
                # Calculate the middle index of the current search range
                mid = (l + r) // 2

                # Update res with the smaller of the current res and nums[mid]
                res = min(nums[mid], res)

                # Determine which half of the array to search next
                if nums[mid] >= nums[l]:  
                    # If nums[mid] is greater than or equal to nums[l], the left half is sorted
                    # The minimum must be in the right half
                    l = mid + 1
                else:
                    # Otherwise, the minimum must be in the left half
                    r = mid - 1
        
        # Return the minimum value found
        return res
