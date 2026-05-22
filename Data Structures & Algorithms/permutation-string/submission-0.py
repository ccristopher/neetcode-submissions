class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        if window_size > len(s2):
            return False

        my_map = {}
        for c in s1:
            my_map[c] = my_map.get(c, 0) + 1
        
        i = 0
        for j in range(len(s2)):
            if s2[j] in my_map:
                my_map[s2[j]] -= 1
            if j - i + 1 > window_size:
                if s2[i] in my_map:
                    my_map[s2[i]] += 1
                i += 1
            if max(my_map.values()) == 0:
                return True
        return False