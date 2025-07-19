class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        q = []
        for i in range(len(nums)):
            num = str(nums[i])
            temp = ''
            for x in num:
                temp += chr( mapping[ord(x) - ord('0')] + ord('0') )
            heapq.heappush(q, (int(temp), i, int(num)))
        #print(q)
        ans = []
        while q:
            _,_,num = heapq.heappop(q)
            ans.append(num)
        return ans