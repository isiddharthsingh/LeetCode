class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers, sp and tp, to the start of strings s and t respectively
        sp, tp = 0, 0

        # Continue until either pointer reaches the end of its string
        while sp < len(s) and tp < len(t):
            # If the characters at the two pointers are the same
            if s[sp] == t[tp]:
                # Move the pointer sp to the next character in s
                sp += 1
            # Move the pointer tp to the next character in t
            tp += 1
        # If all characters in s are found in t in the same order, return True
        # Otherwise, return False
        return sp == len(s)
