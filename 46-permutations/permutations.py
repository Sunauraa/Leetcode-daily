class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        per = []

        def dequy(index):
            for i in nums:
                if i in per:
                    continue
                per.append(i)
                #print(per)
                if len(per) == n:
                    ans.append(per.copy())
                    #print(ans)
                else:
                    dequy(index+1)
                per.remove(i)
        
        dequy(1)
        #print(ans)
        return ans