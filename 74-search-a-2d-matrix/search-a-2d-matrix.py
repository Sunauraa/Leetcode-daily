class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ansi = 0
        l,r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] > target:
                r = mid -1
            else:
                ansi = mid
                l = mid + 1
        ansj = 0
        l,r = 0, len(matrix[0])-1
        while l <= r:
            mid = (l+r)//2
            if matrix[ansi][mid] > target:
                r = mid - 1
            else:
                ansj = mid
                l = mid + 1
        return matrix[ansi][ansj] == target