class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort( key = lambda x: (-x[0],x[1]))
        ans = []
        for x in people:
            ans.insert(x[1],x)
        return ans
