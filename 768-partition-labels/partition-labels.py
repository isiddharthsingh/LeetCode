class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}  # Initialize a dictionary to store the last index of each character

        # Populate the dictionary with the last occurrence index of each character
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []  # Initialize a list to store the partition sizes
        size, end = 0,0  # Initialize variables for the current partition size and end index

        for i, c in enumerate(s):
            size += 1  # Increment the partition size
            end = max(end, lastIndex[c])  # Update the end index based on the last occurrence

            if i == end:
                # If the current index reaches the end index, complete the partition
                res.append(size)
                size = 0  # Reset the partition size for the next segment

        return res
