class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cur = 0
        res = 0
        for s in bank:
            cnt = s.count('1')
            if not cnt:
                continue
            res+= cur*cnt
            cur = cnt
        return res