class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if len(s) == 0: return 0
        # print(s)
        ans = ""
        temp = 1
        if s[0] == '-':
            temp = -1 
            s = s[1:]
        elif s[0] == "+":
            temp = 1
            s = s[1:]
        # print(s)
        for i in range(len(s)):
            # print(i)
            if s[i].isdigit(): 
                ans += s[i]
            elif s[i].isdigit()==False:
                break

        print(ans)
        if len(ans) > 0:
            min_int = -2147483648
            max_int = 2147483647    
            num = int(ans)*temp
            if num < min_int:
                num = min_int
            elif num > max_int:
                num = max_int
            return(num)
        else: return 0