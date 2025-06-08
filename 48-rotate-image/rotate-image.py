class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range( 1, 2*n - 2 ):
            j = i
            k = 0
            while j >= n:
                #print(i)
                j-=1
                k+=1
                #print(j,k)
            check = (j + k)//2
            while k <= check:
                print(matrix[k][j], matrix[j][k])
                matrix[k][j], matrix[j][k] = matrix[j][k], matrix[k][j]
                k+=1
                j-=1
        for i in range(n):
            matrix[i][:] = matrix[i][::-1]

        