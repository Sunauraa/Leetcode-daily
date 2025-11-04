class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        m = defaultdict(int)
        n = len(nums)
        ans = []

        def count():
            store = SortedList([ [v,k] for k,v in m.items() ])
            sm = 0
            #print(store)
            for j in range( max(0,len(store)-x), len(store)):
                sm += store[j][1]*store[j][0]
            #print(sm)
            return sm


        for i in range(n):
            m[nums[i]]+=1
            if i >= k - 1:
                cnt = count()
                ans.append(cnt)
                #print(m,cnt)
                m[nums[i-k+1]]-=1
        return ans
                
