class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_column = n
        for row, column in ops:
            min_row = min(min_row, row)
            min_column = min(min_column, column)
        return min_row*min_column        