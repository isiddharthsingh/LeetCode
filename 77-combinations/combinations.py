class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # This will hold all the possible combinations
        res = []

        # Define a helper function for backtracking
        def backtrack(start, comb):
            # If the combination reaches the required length (k), add it to the results
            if len(comb) == k:
                # Make a copy of the combination and append it to the results
                res.append(comb[::])  # Using comb[::] to create a shallow copy
                return
            
            # Iterate through the range starting from 'start' to 'n'
            for i in range(start, n + 1):
                # Add the current number to the combination
                comb.append(i)
                # Continue building the combination with the next numbers
                backtrack(i + 1, comb)
                # Remove the last number added to backtrack and try other numbers
                comb.pop()
        
        # Start the backtracking process from 1 with an empty combination
        backtrack(1, [])
        return res
