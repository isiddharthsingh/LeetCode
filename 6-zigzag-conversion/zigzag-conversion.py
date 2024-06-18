class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is 1, return the original string
        if numRows == 1: return s

        # Initialize the result string
        res = ""
        
        # Iterate over each row
        for r in range(numRows):
            # Calculate the increment for the current row
            increment = 2*(numRows-1)
            
            # Iterate over the string with the calculated increment
            for i in range(r,len(s),increment):
                # Add the character at the current index to the result
                res += s[i]
                
                # If the row is not the first or last row and the next index is within the string length
                if (r>0 and r <numRows -1 and i+increment-2*r <len(s)):
                    # Add the character at the next index to the result
                    res += s[i+increment-2*r]
                    
        # Return the result
        return res
