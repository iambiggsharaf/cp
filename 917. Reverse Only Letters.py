class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = ""
        news = ""
        for i in s:
            if "a" <= i <= 'z' or "A" <= i <= "Z":
                ans += i
                news += " "
            else: 
                news += i
        ans = ans[::-1]
        ind = 0
        result = ""
        for i in news:
            if i == " ":
                result += ans[ind]
                ind += 1
            else:
                result += i
        
        return result