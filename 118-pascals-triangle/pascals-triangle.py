class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(2,numRows+1):
            temp = [0]*i
            temp[0] = 1
            temp[i-1] = 1
            for x in range(1,i-1):
                temp[x] = res[i-2][x-1] + res[i-2][x]
            res.append(temp)
        return res