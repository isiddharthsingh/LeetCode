from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to keep track of numbers
        stack = []
        
        # Iterate through each token in the input list
        for c in tokens:
            # If the token is a '+', perform addition with the top two elements of the stack
            if c == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)
            # If the token is a '-', perform subtraction with the top two elements of the stack
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            # If the token is a '*', perform multiplication with the top two elements of the stack
            elif c == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(a*b)
            # If the token is a '/', perform integer division with the top two elements of the stack
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  # Use int() to truncate towards zero
            # If the token is a number, convert it to an integer and push it onto the stack
            else:
                stack.append(int(c))
        
        # The result of the expression will be the only element left in the stack
        return stack[0]
