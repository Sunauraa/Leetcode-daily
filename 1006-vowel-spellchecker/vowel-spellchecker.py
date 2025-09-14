class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        caseMap = {}
        vowelMap = {}

        def deVowel(s):
            return ''.join('*' if c in 'aeiou' else c for c in s)

        for w in wordlist:
            lower = w.lower()
            devowel = deVowel(lower)
            if lower not in caseMap:
                caseMap[lower] = w
                if devowel not in vowelMap:
                    vowelMap[devowel] = w
        
        result = []
        for q in queries:
            if q in exact:
                result.append(q)
            else:
                lower = q.lower()
                devowel = deVowel(lower)
                if lower in caseMap:
                    result.append(caseMap[lower])
                elif devowel in vowelMap:
                    result.append(vowelMap[devowel])
                else:
                    result.append("")
        return result