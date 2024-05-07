class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()  # Initialize a set to track which indices are "good"

        for t in triplets:
            # Check if any component of the triplet exceeds the corresponding target value
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue  # Skip this triplet if it doesn't meet the criteria
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)  # Mark the index as "good" if the component matches the target

        # Return True if all three indices are marked as "good"
        return len(good) == 3
