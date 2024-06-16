class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize an empty string to store the common prefix
        res = ""

        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            # Check if the current character is the same in all strings
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    # If not, return the current common prefix
                    return res
            # Otherwise, add the character to the common prefix
            res += strs[0][i]

        # Return the final common prefix
        return res
