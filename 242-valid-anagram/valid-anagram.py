class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If s and t have different lengths, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Initialize two dictionaries to count the occurrences of each character in s and t
        countS, countT = {}, {}

        # Iterate over the characters in s and t
        for i in range(len(s)):
            # Increment the count of the current character in s
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # Increment the count of the current character in t
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Check if the character counts are the same for s and t
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        # If we have checked all characters without returning False, then s and t are anagrams
        return True
