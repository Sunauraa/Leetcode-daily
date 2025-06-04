class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[len(arr)-1])
        