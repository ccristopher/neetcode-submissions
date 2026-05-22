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
        reslen = float('inf')
        i = 0
        need = len(freq_map)
        for j in range(len(s)):
            if s[j] in freq_map:
                freq_map[s[j]] -= 1
                if freq_map[s[j]] == 0:
                    need -= 1
            
            while need == 0:
                if j + 1 - i < reslen:
                    res = [i, j + 1]
                    reslen = j + 1 - i
                if s[i] in freq_map:
                    freq_map[s[i]] += 1
                    if freq_map[s[i]] > 0:
                        need += 1
                i += 1
        
        if res == [-1, -1]:
            return ""
        return s[res[0]: res[1]]