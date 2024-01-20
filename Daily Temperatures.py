class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = [] # [temp,index]

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #-1 for last element, 0 for the temp because temp is at 0 index in stack [temp,index]
                stackT, stackI = stack.pop()
                res[stackI] = (i-stackI)
            stack.append([t,i])
        return res