class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l , r = 1, num

        while l<=r:
            m = (l+r)//2
            m_squared = m*m
            if num == m_squared:
                return True
            elif m_squared < num:
                l = m+1
            else:
                r = m-1
        return False # Time: O(log n),Space O(1)