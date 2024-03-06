class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Early return if s1 is longer than s2
        if len(s1) > len(s2):
            return False
        
        # Initialize character count arrays for s1 and s2
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Populate the initial counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        
        # Slide the window across s2 and check if any permutation matches
        for i in range(len(s2) - len(s1)):
            if s1_count == window_count:
                return True
            # Move the window: remove the leftmost character and add the next character
            window_count[ord(s2[i]) - ord('a')] -= 1
            window_count[ord(s2[i + len(s1)]) - ord('a')] += 1
        
        # Check the last window position after the loop
        return s1_count == window_count
