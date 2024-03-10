class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = []
        l,r = 0,0

        while r < len(nums):
            #pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #remove left val from window
            if l > q[0]:
                q.pop(0)
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output