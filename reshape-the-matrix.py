class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        list = []
        ans = []
        for row in mat:
            for column in row:
                list.append(column)

        for i in range(0, len(list), c):
            ans.append(list[i:i+c])
        return ans                
        