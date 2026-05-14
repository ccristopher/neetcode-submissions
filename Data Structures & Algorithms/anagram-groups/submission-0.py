class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create an empty list of hashmaps
        # create an empty list of sublists of items
        # for each item in strs,
        # hash item with character frequency
        # check our hash list to see if our hash exists
        # if it does add it to the list of sublists of items
        # if it doesnt add the hash into the list of hashmaps and add item to sublist of items

        # return sublist of items

        hash_list = []
        item_list = []
        for item in strs:
            anagram = {}
            for c in item:
                if c in anagram:
                    anagram[c] += 1
                else:
                    anagram[c] = 1
            found = False
            for i in range(len(hash_list)):
                if hash_list[i] == anagram:
                    item_list[i].append(item)
                    found = True
            if not found:
                hash_list.append(anagram)
                item_list.append([item])
        
        return item_list