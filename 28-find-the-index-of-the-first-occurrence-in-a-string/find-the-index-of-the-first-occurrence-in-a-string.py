class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If the needle is an empty string, return 0
        if needle == "":
            return 0 
        
        # Iterate over the haystack string
        for i in range(len(haystack)+1 -len(needle)):
            # Check if the substring of haystack from index i to i+len(needle) is equal to needle
            if haystack[i:i+len(needle)] == needle:
                # If it is, return the current index i
                return i
                
        # If the needle is not found in the haystack, return -1
        return -1
