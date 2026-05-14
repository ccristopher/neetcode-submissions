class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = defaultdict(list)
        for item in strs:
            char_count = [0] * 26
            for c in item:
                char_count[ord(c) - ord('a')] += 1
            hash_dict[tuple(char_count)].append(item)
        
        return list(hash_dict.values())