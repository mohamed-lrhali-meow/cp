def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())

for _ in range(n): 
    t = 2
    x = int(input())
    nums= list(map(int,input().split()))
    out = 0
    while out == 0 : 
        for i in nums : 
            if get_gcd(t , i) == 1 : 
                out = t 
                print(out)
                break
        t += 1