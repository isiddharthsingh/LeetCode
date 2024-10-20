class TrieNode:
    def __init__(self):
        # Initialize a dictionary to hold child nodes
        self.children = {}
        # Boolean flag to mark the end of a word
        self.endOfWord = False

class Trie:

    def __init__(self):
        # Initialize the root node of the Trie
        self.root = TrieNode()
                
    def insert(self, word: str) -> None:
        # Start from the root node
        curr = self.root
 
        # Iterate through each character in the word
        for c in word:
            # If the character is not in the current node's children, add it
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # Move to the child node
            curr = curr.children[c]
        # Mark the end of the word
        curr.endOfWord = True        

    def search(self, word: str) -> bool:
        # Start from the root node
        curr = self.root 
        # Iterate through each character in the word
        for c in word:
            # If the character is not in the current node's children, return False
            if c not in curr.children:
                return False
            # Move to the child node
            curr = curr.children[c]
        # Return True if the current node marks the end of a word
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        curr = self.root
        # Iterate through each character in the prefix
        for c in prefix:
            # If the character is not in the current node's children, return False
            if c not in curr.children:
                return False
            # Move to the child node
            curr = curr.children[c]
        # Return True if all characters in the prefix are found
        return True        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)