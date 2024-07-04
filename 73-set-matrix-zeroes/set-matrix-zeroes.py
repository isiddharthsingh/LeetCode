class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Approach 2 without using Space
        col0 = 1
        m,n = len(matrix),len(matrix[0])

        #STEP 1 Identify the 0 and mark in the first row and first col
        for i in range(m):
            for j in range(n):
                #checking if the element is 0 then mark the row and column
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j != 0: # simce col0 is another variable so marking it explicitly
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        
        #STEP 2: Now you have the marked array on row0 and col0 so, traverse the rest of matrix
        
        for i in range(1,m):
            for j in range(1,n):
                # first i will check the matrix if there is any then simply 0 else we will 
                #check for first row and first column that we have marked
                if matrix[i][j] != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        
        # Now the remaining first column we are checking
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0
        
        # Now the remaining first row we are checking
        if col0 == 0:
            for j in range(m):
                matrix[j][0] = 0
        









        # # Brute Force approach using space of O(m+n)
        # row,col = [0] * len(matrix),[0] * len(matrix[0])
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             row[i],col[j] = 1,1
        
        # print(row,col)

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if row[i] == 1 or col[j] == 1:
        #             matrix[i][j] = 0