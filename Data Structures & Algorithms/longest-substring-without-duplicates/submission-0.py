class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        max_len = 0 
        for i in range(len(s)): 
            if s[i] not in sub: 
                sub += s[i]
            else: 
                sub = sub[sub.index(s[i])+1:]
                sub += s[i]
            if len(sub) > max_len : max_len = len(sub)
        return max_len