class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions = SortedList(potions)
        n = len(potions)
        for i in spells:
            num = potions.bisect_left( success//i + (success%i != 0) )
            res.append(n-num)
        return res