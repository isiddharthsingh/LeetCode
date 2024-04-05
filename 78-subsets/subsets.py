class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i=0):
    
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            #decision to include nums[i]
            subset.append(nums[i])
            #move to next num
            dfs(i+1)

            #decision not to include nums[i]
            #pop the element recently added
            subset.pop()
            dfs(i+1)

        dfs()
        return res