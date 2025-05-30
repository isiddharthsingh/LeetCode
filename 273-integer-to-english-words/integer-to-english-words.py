class Solution:
    def numberToWords(self, num: int) -> str:
        # Special case for 0
        if num == 0:
            return "Zero"

        # Words for numbers less than 20
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        # Words for multiples of ten
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]

        # Scale names for thousands
        scales = ["", "Thousand", "Million", "Billion"]

        # Helper function to convert numbers less than 1000
        def convertChunk(n):
            result = ""

            # If number has hundreds place
            if n >= 100:
                result += below_20[n // 100] + " Hundred "
                n %= 100  # remove the hundreds part

            # If number is 20 or more, handle tens and ones
            if n >= 20:
                result += tens[n // 10] + " "
                n %= 10

            # Handle numbers below 20
            if n > 0:
                result += below_20[n] + " "

            return result

        result = ""        # final result string
        scaleIndex = 0     # index to track the scale ("", "Thousand", etc.)

        # Process the number in 3-digit chunks from right to left
        while num > 0:
            chunk = num % 1000  # Get last 3 digits
            if chunk != 0:
                # Convert chunk and add the appropriate scale (e.g., Thousand)
                words = convertChunk(chunk)
                result = words + scales[scaleIndex] + " " + result
            num //= 1000  # Remove last 3 digits
            scaleIndex += 1  # Move to the next scale

        # Return the result with extra spaces stripped
        return result.strip()