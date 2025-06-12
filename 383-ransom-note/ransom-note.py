class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = defaultdict(int)
        for i in magazine:
            m[i]+=1
        for i in ransomNote:
            m[i]-=1
            if m[i] < 0:
                return False
        return True
        