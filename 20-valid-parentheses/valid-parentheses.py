class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        # Create a mapping of closing brackets to their corresponding opening brackets
        mapper = {"}":"{",")":"(","]":"["}

        # Iterate through each character in the string
        for paran in s:
            # If the character is a closing bracket
            if paran in mapper:
                # Check if the stack is empty or the top of the stack doesn't match the corresponding opening bracket
                if not stack or mapper[paran] != stack[-1]:
                    return False
                else:
                    # If it matches, pop the top of the stack
                    stack.pop()
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(paran)
        
        # If the stack is empty, all brackets were matched correctly
        return stack == []
