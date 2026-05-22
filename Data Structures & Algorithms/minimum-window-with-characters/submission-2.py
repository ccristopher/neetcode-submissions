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

        
        res = [-1, -1]
        i = 0
        for j in range(len(s)):
            if s[j] in freq_map:
                freq_map[s[j]] -= 1
            
            while max(freq_map.values()) == 0:
                substr = [i, j + 1]
                if res == [-1, -1]:
                    res = substr
                elif j + 1 - i < res[1] + 1 - res[0]:
                    res = substr
                if s[i] in freq_map:
                    freq_map[s[i]] += 1
                i += 1
        
        if res == [-1, -1]:
            return ""
        return s[res[0]: res[1]]