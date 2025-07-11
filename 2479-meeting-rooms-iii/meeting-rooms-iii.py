class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        queue = []
        opn = []
        for i in range(n):
            opn.append(i)
        meetings.sort()
        #print(meetings)
        arr = [0]*n
        for start,end in meetings:
            time,num = -1, -1
            """print(queue)
            print(opn)
            print('|')"""
            while queue and queue[0][0] <= start:
                pos = bisect.bisect_left(opn, queue[0][1])
                opn.insert(pos, queue[0][1])
                #opn.add(queue[0][1])
                queue.remove( queue[0] )
            if opn:
                #print(opn)
                for x in opn:
                    num = x
                    break
                opn.remove(num)
            else:
                time,num = queue[0]
                queue.remove(queue[0])
            arr[num]+=1
            new = 0
            if time != -1:
                new = (time +(end-start),num)
            else:
                new = (end,num)
            pos = bisect.bisect_left(queue, new)
            queue.insert(pos, new)
            """print(queue)
            print(opn)
            print()"""
        #print(arr)
        mx = max(arr)
        for i in range(n):
            if arr[i] == mx:
                return i
        