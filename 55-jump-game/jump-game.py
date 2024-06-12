class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the goal position as the last index
        goal = len(nums) - 1

        # Iterate through the array in reverse
        for i in range(len(nums) - 1, -1, -1):
            # If the current position plus the jump distance can reach the goal,
            # update the goal position to the current index
            if i + nums[i] >= goal:
                goal = i

        # If the goal position reaches the start (index 0), return True; otherwise, return False
        return True if goal == 0 else False
