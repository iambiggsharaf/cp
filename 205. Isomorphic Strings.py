a = input()
b = input()
foo = {}
flag1 = True
flag2 = True

for i in range(len(a)):
    if a[i] not in foo:
        foo[a[i]] = b[i]
    else:
        if foo[a[i]]!=b[i]:
            flag1 = False
            
        
# print(foo)

a, b = b, a
foo = {}
for i in range(len(a)):
    if a[i] not in foo:
        foo[a[i]] = b[i]
    else:
        if foo[a[i]]!=b[i]:
            flag2 = False
            
        
# print(foo)

print(flag1 and flag2)