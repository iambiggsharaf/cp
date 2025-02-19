t = int(input())
for _ in range(t):
    h, m = [int(i) for i in input().split(":")]
    if h == 0: print(12, ":", m//10, m%10, " AM", sep="")
    if 1 <= h <= 11: print(h//10, h%10, ":", m//10, m%10, " AM", sep="")
    if h == 12: print(12, ":", m//10, m%10, " PM", sep="")
    if 13 <= h <= 23: print((h-12)//10, (h-12)%10, ":", m//10, m%10, " PM", sep="")