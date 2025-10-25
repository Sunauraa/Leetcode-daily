class Solution:
    def totalMoney(self, n: int) -> int:
        cnt = 0
        prevMon = 1
        nxMon = 1
        while n > 7:
            prevMon = nxMon
            nxMon+=1
            cnt+= (prevMon+6)*(prevMon+7)//2 - (prevMon-1)*(prevMon)//2
            n-=7
            #print(cnt)
        if n > 0:
            prevMon = nxMon
            #print(prevMon,n)
            cnt+= (prevMon+n-1)*(prevMon+n)//2 - (prevMon-1)*(prevMon)//2
        return cnt

            