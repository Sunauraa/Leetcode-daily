class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cur = 1
        lengths = []
        for o in operations:
            cur*=2
            lengths.append(cur)
            if cur >= k:
                break
        shift = 0
        for i in range(len(lengths)-1,-1,-1):
            half = lengths[i]//2
            if k > half:
                k-=half
                if operations[i]==1:
                    shift+=1
        return chr(shift%26 + ord('a'))

        