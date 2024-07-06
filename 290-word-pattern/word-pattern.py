class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string into words
        words = s.split(" ")
        
        # If the pattern and the words list don't have the same length, they can't be isomorphic
        if len(pattern) != len(words):
            return False
        
        # Initialize two dictionaries to map characters from pattern to words and vice versa
        charToWord, wordToChar = {}, {}

        # Iterate over the characters in pattern and words simultaneously
        for c, w in zip(pattern, words):
            # If the current character in pattern is already mapped to a different word
            # or the current word is already mapped to a different character in pattern
            # then pattern and words are not isomorphic
            if ((c in charToWord and charToWord[c] != w) or 
                (w in wordToChar and wordToChar[w] != c)):
                return False
            
            # Add the current character and word to the mappings
            charToWord[c] = w
            wordToChar[w] = c

        # If we have iterated over all characters without returning False, then pattern and words are isomorphic
        return True
