class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        L,R=0, ROWS*COLS-1
        while L<=R:
            M=(L+R)//2
            i=M//COLS
            j=M%COLS
            mid_sum=matrix[i][j]
            if target > mid_sum:
                L=M+1
            elif target < mid_sum:
                R=M-1
            else:
                return True

        return False