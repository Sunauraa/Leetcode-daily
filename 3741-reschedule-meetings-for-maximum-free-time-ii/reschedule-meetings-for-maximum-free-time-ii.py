class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        cur = 0
        time = []
        for start,end in zip(startTime,endTime):
            time.append(start - cur)
            time.append(end-start)
            cur = end
        time.append(eventTime - cur)

        mxlf = [0]*(len(time))
        for i in range(0, len(time), 2):
            if i == 0:
                mxlf[i] = time[i]
            else:
                mxlf[i] = max(mxlf[i-2],time[i])

        mxrt = [0]*(len(time))
        for i in range(len(time)-1, -1, -2):
            if i == len(time) - 1:
                mxrt[i] = time[i]
            else:
                mxrt[i] = max(mxrt[i+2], time[i])

        ans = 0
        for i in range( 1 , len(time), 2 ):
            ans = max(ans, time[i-1] + time[i+1])
            if (i >= 0 and time[i] <= mxlf[i-3]) or ( i + 3 < len(time) and time[i] <= mxrt[i+3]):
                ans = max(ans,time[i-1]+time[i] + time[i+1])

        return ans