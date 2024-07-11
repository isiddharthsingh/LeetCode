class Solution:
    def calculate(self, s: str) -> int:
        # Initialize a stack to keep track of intermediate results and signs
        stack = []
        # Initialize the current number and the current result
        current_number = 0
        result = 0
        # Start with a positive sign
        sign = 1

        # Iterate over each character in the string
        for char in s:
            if char.isdigit():
                # Construct the current number by shifting the digits left and adding the new digit
                current_number = current_number * 10 + int(char)
            elif char == '+':
                # Add the current number to the result with the current sign
                result += sign * current_number
                # Reset the current number and update the sign
                current_number = 0
                sign = 1
            elif char == '-':
                # Subtract the current number from the result with the current sign
                result += sign * current_number
                # Reset the current number and update the sign
                current_number = 0
                sign = -1
            elif char == '(':
                # Push the result and the sign onto the stack
                stack.append(result)
                stack.append(sign)
                # Reset the result for the new sub-expression
                result = 0
                # Reset the sign to positive
                sign = 1
            elif char == ')':
                # Add the current number to the result with the current sign
                result += sign * current_number
                # Reset the current number
                current_number = 0
                # Pop the sign from the stack and multiply with the result
                result *= stack.pop()
                # Pop the previous result from the stack and add it to the current result
                result += stack.pop()

        # Add the last number to the result
        result += sign * current_number
        return result
