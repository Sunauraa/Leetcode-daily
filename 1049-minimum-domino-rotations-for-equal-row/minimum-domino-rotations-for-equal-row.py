class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = -1
        n = len(tops)
        cnt = 0
        temp = tops[0]
        check = 1
        dub = 0
        for i in range(n):
            if tops[i] == temp or bottoms[i] == temp:
                if  tops[i] != temp:
                    cnt+=1
                if tops[i] == bottoms[i]:
                    dub+=1
            else:
                check = 0
                break
        if check:
            ans = min(n-cnt - dub, cnt)
            return ans
        temp = bottoms[0]
        check = 1
        dub = 0
        cnt = 0
        for i in range(n):
            if tops[i] == temp or bottoms[i] == temp:
                if bottoms[i] != temp:
                    cnt+=1
                if bottoms[i] == tops[i]:
                    dub+=1
            else:
                check = 0
                break
        if check:
            ans = min(cnt, n - cnt - dub)
        return ans