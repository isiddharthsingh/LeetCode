class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store the numbers in nums as keys and their indices as values
        hashmap = {} #value: index

        # Iterate over the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - num
            # If the difference is in the hashmap, we have found two numbers such that they add up to the target
            if diff in hashmap:
                # Return the indices of the two numbers
                return [hashmap[diff], i]
            # If the current number is not in the hashmap, add it with its index
            hashmap[num] = i
