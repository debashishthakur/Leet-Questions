class Solution:
    def isPalindrome(self, s: str):
        
        string = ''.join(filter(str.isalnum, s))
        str_rev = ""
        for i in string:
            str_rev = i + str_rev
        if string.lower() == str_rev.lower():
            return True
        else:
            return False
                
