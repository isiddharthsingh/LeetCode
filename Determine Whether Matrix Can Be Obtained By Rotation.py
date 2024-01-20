from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
        return False

    def rotate(self, mat: List[List[int]]) -> None:
        l, r = 0, len(mat) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the top-left
                topLeft = mat[top][l + i]

                # move bottom-left into top-left
                mat[top][l + i] = mat[bottom - i][l]

                # move bottom-right into bottom-left
                mat[bottom - i][l] = mat[bottom][r - i]

                # move top-right into bottom-right
                mat[bottom][r - i] = mat[top + i][r]

                # move top-left into top-right
                mat[top + i][r] = topLeft

            r -= 1
            l += 1