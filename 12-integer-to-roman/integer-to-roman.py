class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of Roman numeral symbols and their corresponding values
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
                   ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                   ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        # Initialize an empty string to store the Roman numeral representation
        res = ""
        
        # Iterate through the symbols in reverse order
        for sym, val in reversed(symList):
            # Check how many times the current value can be subtracted from num
            if num // val:
                count = num // val
                res += sym * count  # Add the corresponding symbol to the result
                num = num % val  # Update the remaining value
        
        # Return the final Roman numeral representation
        return res
