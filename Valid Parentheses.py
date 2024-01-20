class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {"}":"{",")":"(","]":"["}

        for paran in s:
            if paran in mapper:
                if not stack or mapper[paran] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(paran)
        
        return stack == []