class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gap = []
        cur = 0
        for start,end in zip(startTime, endTime):
            gap.append(start - cur)
            cur = end
        if eventTime - cur:
            gap.append(eventTime - cur)
        ans = 0
        s = 0
        for i in range(len(gap)):
            s+=gap[i]
            ans = max(ans,s)
            if i >= k:
                s-=gap[i-k]
        return ans