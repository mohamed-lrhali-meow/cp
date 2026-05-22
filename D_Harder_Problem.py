import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x = int(input())
    a = list(map(int, input().split()))
    b = []
    seen = set()
    a_set = set(a)
    filler = 1
    # advance filler to first unused value
    while filler <= x and filler in a_set:
        filler += 1
    
    for i in range(x):
        if a[i] not in seen:
            b.append(a[i])
            seen.add(a[i])
        else:
            b.append(filler)
            seen.add(filler)
            filler += 1
            while filler <= x and filler in a_set:
                filler += 1
    
    sys.stdout.write(' '.join(map(str, b)) + '\n')