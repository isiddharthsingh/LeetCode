class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """result = []

        #base case
        if(len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            
            result.extend(perms)
            nums.append(n)

        return result"""

        res = []

        # Backtracking function to generate permutations
        def backtrack(path, remaining):
            # If the path contains all numbers, it's a valid permutation
            if not remaining:
                res.append(path[:])  # Add a copy of the path to the results
                return
            
            # Iterate through the remaining numbers
            for i in range(len(remaining)):
                # Choose the current number
                path.append(remaining[i])
                # Explore with the chosen number removed from the remaining numbers
                backtrack(path, remaining[:i] + remaining[i+1:])
                # Backtrack: remove the last number added to try other options
                path.pop()

        # Start backtracking with an empty path and the full list of numbers
        backtrack([], nums)
        return res