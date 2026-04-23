class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while True : 
            if left >= right: break  
            if (s[left] + s[right]).isalnum() : 
                if s[left].lower() != s[right].lower(): return False 
                else : 
                    left +=1 
                    right -=1
            if s[left].isalnum() == False : 
                left +=1 
            if s[right].isalnum() == False:
                right -=1 
        return True
            