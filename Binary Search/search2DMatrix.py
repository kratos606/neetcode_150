class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            m = (l + r) // 2
            mr, mc = m // cols, m % cols
            if target < matrix[mr][mc]:
                r = m - 1
            elif target > matrix[mr][mc]:
                l = m + 1
            else:
                return True
        
        return False
