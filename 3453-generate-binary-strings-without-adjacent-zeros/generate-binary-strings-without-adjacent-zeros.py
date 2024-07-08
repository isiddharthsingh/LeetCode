class Solution:
    def validStrings(self, n: int) -> List[str]:
        # List to store the results
        results = []
        
        def backtrack(current_string):
            # If the current string has reached the desired length
            if len(current_string) == n:
                results.append(current_string)
                return
            
            # Option to add '1'
            backtrack(current_string + '1')
            
            # Option to add '0', only if the last character is '1'
            if not current_string or current_string[-1] == '1':
                backtrack(current_string + '0')

        # Start the backtracking process with an empty string
        backtrack("")
        return results