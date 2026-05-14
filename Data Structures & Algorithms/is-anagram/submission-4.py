class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_list = [0] * 26 
        for c in s:
            my_list[ord(c) - 97] += 1
        
        for c in t:
            my_list[ord(c) - 97] -= 1
            if my_list[ord(c) - 97] == -1:
                return False
        
        return True