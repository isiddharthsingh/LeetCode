class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert the word list to a set for O(1) lookups
        word_set = set(wordList)

        # If the endWord is not in the word set, return 0
        if endWord not in word_set:
            return 0
        
        # List of all possible characters for transformation
        char_list = 'abcdefghijklmnopqrstuvwxyz'
        # Initialize the queue with the beginWord and step count 1
        queue = deque([(beginWord, 1)])

        while queue:
            # Get the current word and the number of steps from the queue
            curr_word, step = queue.popleft()

            # If the current word is the endWord, return the number of steps
            if curr_word == endWord:
                return step 
            
            # Try changing each character in the current word
            for i in range(len(curr_word)):
                for char in char_list:
                    # Skip if the character is the same as the current one
                    if curr_word[i] == char:
                        continue

                    # Create a new word by changing the current character
                    next_word = curr_word[:i] + char + curr_word[i+1:]

                    # If the new word is in the word set, add it to the queue and remove it from the set
                    if next_word in word_set:
                        queue.append((next_word, step + 1))
                        word_set.remove(next_word)
        
        # If no transformation sequence leads to the endWord, return 0
        return 0
