from sortedcontainers import SortedList

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        window = SortedList()
        poppedIdx = []
        n = len(num)
        remainedIdx = SortedList(range(n))
        while k > 0:
            while len(window) < k + 1 and len(window) < len(remainedIdx):
                idx = remainedIdx[len(window)]
                window.add((num[idx],idx))
            if not window:
                break
            idx = window.pop(0)[1]
            k-= remainedIdx.bisect_left(idx)
            remainedIdx.remove(idx)
            poppedIdx.append(idx)
            for idx in remainedIdx[k+1:len(window)]:
                window.remove((num[idx],idx))
        #poppedSet = set(poppedIdx)
        #print(poppedIdx)
        return ''.join( num[idx] for idx in poppedIdx ) + ''.join(num[idx] for idx in range(n) if idx not in poppedIdx)
