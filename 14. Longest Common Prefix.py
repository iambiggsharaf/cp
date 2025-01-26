class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.append(strs[0] + 'a')
        print(strs)
        if len(strs) == 1:
            # print(strs[0])
            return strs[0]
            exit()
        ans = min(strs, key=len)
        result = ""
        for i in range(len(ans)+1):
            word = ans[:i]
            print(word)
            for j in strs:
                result = str(ans[:i])
                if not j.startswith(word):
                    result = str(ans[:i - 1])
                    return result
        return result
                    
        