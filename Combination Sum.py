class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #cur is a list of values which are being added for calculating the total
        def dfs(i,cur,total):
            if total == target:
                #copy because we don't want to make any changes to the current variable
                res.append(cur.copy())
                return 
            
            if i >= len(candidates) or total > target:
                return
            
            # if you want to include the same "i" again
            cur.append(candidates[i])
            # call the dfs function to make a tree
            dfs(i,cur,total+candidates[i])
            # pop it before calling the dfs 
            cur.pop()
            #again call the dfs func to make the tree if we don't want to include the same value
            dfs(i+1,cur,total)


        dfs(0,[],0)
        return res