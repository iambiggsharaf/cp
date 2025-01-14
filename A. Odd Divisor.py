def isPowerOfTwo(n):
        if n > 0:
            while n > 1:
                if n % 2 != 0: 
                    return False
                n //= 2
            return True
        return False
t = int(input())
for _ in range(t):
    n = int(input())
    if isPowerOfTwo(n): print("NO")
    else: print("YES")
        