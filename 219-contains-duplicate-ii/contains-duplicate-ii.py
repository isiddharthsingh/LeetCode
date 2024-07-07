class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initialize a dictionary to store the numbers in nums as keys and their indices as values
        dict = {}

        # Iterate over the list of numbers with their indices
        for i in range(len(nums)):
            # If the current number is in the dictionary and the difference between its current index and the stored index is less than or equal to k
            if nums[i] in dict and i - dict[nums[i]] <= k:
                # Return True because we have found a duplicate within k distance
                return True
            # If the current number is not in the dictionary or the stored index is too far, update the index
            dict[nums[i]] = i

        # If we have iterated over all numbers without returning True, then there are no duplicates within k distance
        return False
