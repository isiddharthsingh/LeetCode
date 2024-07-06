class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize two dictionaries to map characters from s to t and vice versa
        mapST, mapTS = {}, {}

        # Iterate over the characters in s and t simultaneously
        for c1, c2 in zip(s, t):
            # If the current character in s is already mapped to a different character in t
            # or the current character in t is already mapped to a different character in s
            # then s and t are not isomorphic
            if ((c1 in mapST and mapST[c1] != c2) or 
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            # Add the current characters to the mappings
            mapST[c1] = c2
            mapTS[c2] = c1
        # If we have iterated over all characters without returning False, then s and t are isomorphic
        return True
