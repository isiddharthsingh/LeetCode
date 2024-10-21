class TrieNode:
    def __init__(self):
        # A dictionary to hold the children nodes for each character and a boolean to mark the end of a word
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        # Initialize the root of the trie
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        # Start at the root of the trie
        curr = self.root

        # Iterate through each character in the word
        for c in word:
            # If the character is not present in the current node's children, create a new node
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # Move to the next node (the child corresponding to the current character)
            curr = curr.children[c]
        # After all characters are processed, mark the end of the word
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # Helper function to perform DFS for search
        def dfs(j, root):
            # Start DFS at the given node (root for the first call)
            curr = root

            # Iterate through the characters in the word starting at index j
            for i in range(j, len(word)):
                c = word[i]
                # If the current character is a dot (wildcard), check all possible children
                if c == ".":
                    # Try matching each child of the current node
                    for child in curr.children.values():
                        # Recursively search from the next character position and the current child
                        if dfs(i + 1, child):
                            return True
                    # If no match is found for any child, return False
                    return False
                else:
                    # If the character is not a dot, check if it exists in the current node's children
                    if c not in curr.children:
                        return False
                    # Move to the child corresponding to the current character
                    curr = curr.children[c]
            # At the end of the word, check if the current node marks the end of a word
            return curr.endOfWord
        
        # Call the DFS function starting from index 0 and the root node
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
