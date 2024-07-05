class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Dictionary to count characters in the magazine
        char_count = {}
        
        # Count each character in the magazine
        for char in magazine:
            # If the character is already in the dictionary, increment its count
            if char in char_count:
                char_count[char] += 1
            # If the character is not in the dictionary, add it with a count of 1
            else:
                char_count[char] = 1
        
        # Check if ransomNote can be constructed
        for char in ransomNote:
            # If the character is not in the dictionary or its count is zero, return False
            if char not in char_count or char_count[char] == 0:
                return False
            # If the character is in the dictionary and its count is non-zero, decrement its count
            char_count[char] -= 1
        
        # If all characters in ransomNote are found in the dictionary with sufficient counts, return True
        return True