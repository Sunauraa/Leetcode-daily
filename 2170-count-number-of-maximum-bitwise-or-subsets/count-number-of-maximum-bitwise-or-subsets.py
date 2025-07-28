class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for i in nums:
            mx|=i
        n = len(nums)
        ans = 0
        cur = 0
        store = [0]*18

        def add(x):
            nonlocal cur
            for i in range(17,-1,-1):
                if x >= (1<<i):
                    store[i]+=1
                    if store[i] == 1:
                        cur += (1<<i)
                    x-=(1<<i)
        def remove(x):
            nonlocal cur
            for i in range(17,-1,-1):
                if x >= (1<<i):
                    store[i]-=1
                    if store[i] == 0:
                        cur -= (1<<i)
                    x-=(1<<i)

        def dequy(idx):
            nonlocal cur,ans
            for i in range(2):
                if i:
                    add(nums[idx])
                    if cur == mx:
                        ans+=1
                if idx != n - 1:
                    dequy(idx+1)
                if i:
                    remove(nums[idx])

        dequy(0)
        return ans

