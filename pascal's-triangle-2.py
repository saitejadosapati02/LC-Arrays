class Solution(object):
    def getRow(self, rowIndex):
       res = [1]
       for i in range(rowIndex):
        nextRow = [0] * (len(res)+1)
        for j in range (len(res)):
            nextRow[j] += res[j]
            nextRow[j+1] += res[j]
        res = nextRow
       return res     
