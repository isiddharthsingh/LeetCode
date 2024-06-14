class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numerals to their corresponding values
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                 "D": 500, "M": 1000}
        
        # Initialize the result variable
        res = 0

        # Iterate through the input string
        for i in range(len(s)):
            # If the current Roman numeral is smaller than the next one,
            # subtract its value from the result
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                # Otherwise, add its value to the result
                res += roman[s[i]]
        
        # Return the final result
        return res
