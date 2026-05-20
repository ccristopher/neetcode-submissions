class Solution:

    def encode(self, strs: List[str]) -> str:
        # first 3 digits is length
        # for each string there are 3 digits that give the strings length
        output = ""
        output = str(len(strs)) + '#'
        strings = ""
        for s in strs:
            output += str(len(s)) + '#'
            strings += s
        
        return output + strings


    def decode(self, s: str) -> List[str]:
        len_strs = ""
        i = 0
        while s[i] != '#':
            len_strs += s[i]
            i += 1
        i += 1

        len_strs = int(len_strs)
        

        my_list = [[] for i in range(len_strs)]
        for k in range(len_strs):
            temp = ""
            while s[i] != '#':
                temp += s[i]
                i += 1
            i += 1

            my_list[k] = int(temp)
        
        output = []
        for word_len in my_list:
            final_word = ""
            for j in range(word_len):
                final_word += s[i]
                i += 1
            output.append(final_word)
    
        return output