class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize a stack to store the directories in the path
        stack = []
        # Initialize a string to store the current directory
        curr = ""

        # Iterate over each character in the path
        for c in path + "/":
            # If the current character is a slash, we have reached the end of a directory
            if c == "/":
                # If the current directory is "..", we need to go up one level, so we pop the stack
                if curr == "..":
                    if stack: stack.pop()
                # If the current directory is not empty and not ".", it's a valid directory, so we add it to the stack
                elif curr != "" and curr != ".":
                    stack.append(curr)
                # Reset the current directory
                curr = ""
            else:
                # If the current character is not a slash, we add it to the current directory
                curr += c
        
        # Join the directories in the stack with slashes and return the simplified path
        return "/" + "/".join(stack)
