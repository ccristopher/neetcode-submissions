class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        # keep going until all characters are present
        # if all characters are present record that as the minimum
        # move the left pointer until characters no longer present (remember to keep recording minimum)

        if len(t) > len(s):
            return ""

        freq_map = {}
        for c in t:
            freq_map[c] = freq_map.get(c, 0) + 1
        
        res = ""
        found = False
        i = 0
        for j in range(len(s)):
            if s[j] in freq_map:
                freq_map[s[j]] -= 1
            
            while max(freq_map.values()) == 0:
                substr = s[i: j + 1]
                if not found:
                    res = substr
                found = True
                if len(substr) < len(res):
                    res = substr
                if s[i] in freq_map:
                    freq_map[s[i]] += 1
                i += 1
        
        return res