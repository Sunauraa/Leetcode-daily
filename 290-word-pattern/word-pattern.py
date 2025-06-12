class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(' ')
        n = len(pattern)
        if len(ss) != n:
            return False
        inventory = set()
        m = defaultdict(str)
        for i in range(n):
            if m[pattern[i]]:
                if m[pattern[i]] != ss[i]:
                    return False
            else:
                if ss[i] in inventory:
                    return False
                m[pattern[i]] = ss[i]
                inventory.add(ss[i])
        return True