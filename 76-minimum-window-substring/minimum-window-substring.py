class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is an empty string, return an empty string
        if t == "": return ""

        # Initialize two dictionaries to store the counts of characters in t and the current window
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # Initialize two variables to store the number of characters that have been found and need to be found
        have, need = 0, len(countT)
        # Initialize the result and its length
        res, resLen = [-1, -1], float("infinity")
        # Initialize the left pointer
        l = 0 
        # Iterate over the string with the right pointer
        for r in range(len(s)):
            # Add the character at the right pointer to the window
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # If the character is in t and its count in the window is equal to its count in t
            if c in countT and window[c] == countT[c]:
                # Increment the number of characters that have been found
                have += 1
            
            # While all characters in t have been found
            while have == need:
                # If the length of the current window is less than the length of the result
                if (r - l + 1) < resLen:
                    # Update the result and its length
                    res = [l, r]
                    resLen = (r - l + 1)
                # Remove the character at the left pointer from the window
                window[s[l]] -= 1
                # If the character is in t and its count in the window is less than its count in t
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # Decrement the number of characters that have been found
                    have -= 1
                # Move the left pointer to the right
                l += 1
        # Get the left and right pointers from the result
        l, r = res
        # If the length of the result is not infinity, return the substring of s from l to r
        # Otherwise, return an empty string
        return s[l:r+1] if resLen != float("infinity") else ""
