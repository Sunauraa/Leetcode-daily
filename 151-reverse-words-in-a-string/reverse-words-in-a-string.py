class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr = arr[::-1]
        return ' '.join(arr)
        