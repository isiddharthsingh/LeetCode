class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
    
        # Length of each word in the list
        word_len = len(words[0])
        # Total number of words in the list
        word_count = len(words)
        # Total length of the substring we are looking for
        total_len = word_len * word_count
        # Frequency counter for the words in the list
        word_freq = Counter(words)
        
        result = []
        
        # Iterate through the string with different starting points within the first word_len characters
        for i in range(word_len):
            left = i  # Left pointer of the window
            right = i  # Right pointer of the window
            curr_freq = word_freq.copy()  # Copy of the word frequency counter
            
            # Count of words matched in the current window
            matches = 0
            
            # Slide the window to the right while maintaining its size
            while right + word_len <= len(s):
                word = s[right:right + word_len]  # Get the next word in the window
                right += word_len  # Move the right pointer
                
                # If the word is in the list of words we are looking for
                if word in curr_freq:
                    curr_freq[word] -= 1  # Decrement its frequency in the current window
                    matches += 1
                    
                    # If the word count goes negative, we have an excess of this word
                    while curr_freq[word] < 0:
                        left_word = s[left:left + word_len]
                        curr_freq[left_word] += 1
                        matches -= 1
                        left += word_len
                    
                    # If the number of matches equals the number of words, we have a valid substring
                    if matches == word_count:
                        result.append(left)
                else:
                    # If the word is not in the list, reset the counters and move the left pointer to right
                    curr_freq = word_freq.copy()
                    matches = 0
                    left = right
        
        return result