class Solution:
    def isHappy(self, n: int) -> bool:
        # Initialize a set to store the numbers we have seen
        visit = set()

        # Continue the loop until we see a number that we have seen before
        while n not in visit:
            # Add the current number to the set
            visit.add(n)
            # Update the current number to the sum of the squares of its digits
            n = self.sumOfSquares(n)

            # If the current number is 1, it is a happy number
            if n == 1:
                return True
        # If we exit the loop, the number is not a happy number
        return False
    

    def sumOfSquares(self, n):
        # Initialize the output to 0
        output = 0 
        # Continue the loop until there are no more digits
        while n:
            # Get the last digit of the number
            digit = n % 10
            # Square the digit and add it to the output
            digit = digit ** 2
            output += digit
            # Remove the last digit from the number
            n = n // 10
        # Return the sum of the squares of the digits
        return output
