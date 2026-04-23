class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        left = 0 
        max_len = 0
        for right, char in enumerate(s): 
            if char in lastSeen and lastSeen[char] >= left:
                left = lastSeen[char] +1 
            lastSeen[char] = right 
            max_len = max(max_len, right - left + 1)
        return max_len 
