class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}

        result = 0

        i = 0
        maxf = 0
        for j in range(len(s)):
            char_map[s[j]] = char_map.get(s[j], 0) + 1
            maxf = max(maxf, char_map[s[j]])
            while j - i + 1 - maxf > k:
                char_map[s[i]] -= 1
                i += 1
            
            result = max(result, j - i + 1)
        
        return result