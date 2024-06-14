class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Initialize a list of candies with all values set to 1
        candies = [1] * len(ratings)

        # First pass: Traverse from left to right
        for i in range(1, len(ratings)):
            # If the current rating is higher than the previous one,
            # assign more candies to the current child
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Second pass: Traverse from right to left
        for i in range(len(ratings) - 2, -1, -1):
            # If the current rating is higher than the next one,
            # update the candies for the current child
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Return the total sum of candies assigned
        return sum(candies)
