class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the start and end of the string
        l, r = 0, len(s) - 1

        # Continue until the two pointers meet
        while l < r:
            # Increment the left pointer until a alphanumeric character is found
            while l < r and not self.alnum(s[l]):
                l += 1
            # Decrement the right pointer until a alphanumeric character is found
            while l < r and not self.alnum(s[r]):
                r -= 1
            # If the characters at the two pointers are not the same (ignoring case), return False
            if s[l].lower() != s[r].lower():
                return False
            
            # Move the pointers towards the center
            l += 1
            r -= 1
        # If all pairs of characters are the same, return True
        return True

    def alnum(self, c):
        # Check if the character is alphanumeric
        return ((ord("A") <= ord(c) <= ord("Z")) or 
                (ord("a") <= ord(c) <= ord("z")) or
                (ord("0") <= ord(c) <= ord("9")))
