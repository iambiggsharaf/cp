class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            while n > 1:
                if n % 2 != 0: 
                    return False
                    exit()
                n //= 2
            return True
        return False