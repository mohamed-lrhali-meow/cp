n = int(input())

'''for _ in range(n) : 
    p = input()
    s = input()
    i = 0 
    j = 0 
    ok = True
    while i < len(p) and j < len(s) : 
        if p[i] != s[j] : 
            ok = False
            break
        j += 1 
        if j < len(s) and s[j] == p[i] : 
            if i == len(p) - 1 or p[i+1] != p[i]:
                j += 1
        i += 1
    if ok and i == len(p) and j == len(s):
        print("YES")
    else:
        print("NO")'''


for i in range(n) : 
    p = input()
    s = input()
    ok = True 
    i = 0
    j = 0
    while i < len(p) and j < len(s):
        group_p = 0
        char = p[i]
        while i < len(p) and p[i] == char:
            group_p += 1
            i += 1
        group_s = 0
        while j < len(s) and s[j] == char:
            group_s += 1
            j += 1
        if not (group_p <= group_s <= 2 * group_p):
            ok = False
            break
    if ok and i == len(p) and j == len(s): 
        print("YES")
    else : 
        print("NO")