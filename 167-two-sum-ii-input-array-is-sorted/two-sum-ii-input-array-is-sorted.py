class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the start and end of the list
        l, r = 0, len(numbers) - 1

        # Continue until the two pointers meet
        while l < r:
            # Calculate the sum of the numbers at the two pointers
            currSum = numbers[l] + numbers[r]
            # If the sum is equal to the target
            if currSum == target:
                # Return the indices of the two numbers, incremented by 1
                return [l+1, r+1]
            # If the sum is greater than the target
            elif currSum > target:
                # Move the right pointer to the left
                r -= 1
            # If the sum is less than the target
            else:
                # Move the left pointer to the right
                l += 1
