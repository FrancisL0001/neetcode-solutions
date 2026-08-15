class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s : str, left : int, right : int):
            while left < right: 
                if not s[left].isalnum():
                    left+=1
                elif not s[right].isalnum():
                    right-=1
                else:
                    if not s[left].lower() == s[right].lower():
                        return False
                    else:
                        left+=1
                        right-=1
        
            return True


        left = 0
        right = len(s) - 1 

        while left < right: 
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            else:
                if not s[left].lower() == s[right].lower():
                    if isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1):
                        return True 
                    else:
                        return False
                else:
                    left+=1
                    right-=1

        return True
        