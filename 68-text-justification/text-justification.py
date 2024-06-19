class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Initialize the result list and the current line list
        res = []
        line, length = [], 0
        i = 0 

        # Iterate over the words
        while i < len(words):
            # If adding the next word to the current line would exceed the maxWidth
            if length + len(line) + len(words[i]) > maxWidth:
                # Calculate the extra space needed to reach the maxWidth
                extra_space = maxWidth - length
                # Calculate the number of spaces to add after each word
                spaces = extra_space // max(1, len(line) - 1)
                # Calculate the remaining spaces after evenly distributing the spaces
                remainder = extra_space % max(1, len(line) - 1)

                # Distribute the spaces to the words in the current line
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    # If there are remaining spaces, add one more space to the current word
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                # Join the words in the current line and add the line to the result
                res.append("".join(line))
                # Reset the current line and its length
                line, length = [], 0
            
            # Add the next word to the current line
            line.append(words[i])
            length += len(words[i])
            i += 1

        # Join the words in the last line with a single space between each word
        last_line = " ".join(line)
        # Calculate the trailing spaces needed to reach the maxWidth
        trail_space = maxWidth - len(last_line)
        # Add the trailing spaces to the last line and add the line to the result
        res.append(last_line + " " * trail_space)
        return res
