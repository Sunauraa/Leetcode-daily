class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heapq.heapify(ans)
        cur = 0
        check = True
        while (len(ans) < k or check) and cur < len(nums1):
            check = False
            for j in nums2:
                if len(ans) < k or nums1[cur] + j < -ans[0][0]:
                    check = True
                    if len(ans) == k:
                        heapq.heappop(ans)
                    heapq.heappush(ans, (-(nums1[cur] + j), nums1[cur],j))
            cur+=1

        print(ans)
        res = []
        for i in ans:
            res.append( [i[1], i[2]] )
        return res
