class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0  # Return 0 if string is empty after trimming

        # Step 2: Determine the sign (+ or -)
        sign = 1  # Default sign is positive
        index = 0  # Start parsing from the beginning

        if s[0] == '-':
            sign = -1  # Change to negative
            index += 1
        elif s[0] == '+':
            index += 1  # Skip the '+' sign

        # Step 3: Read digits and form the number
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit  # Shift left and add new digit
            index += 1

        # Step 4: Apply the sign
        result *= sign

        # Step 5: Clamp to 32-bit signed integer range [-2^31, 2^31 - 1]
        INT_MIN = -2**31         # -2147483648
        INT_MAX = 2**31 - 1      #  2147483647

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        # Step 6: Return the final result
        return result