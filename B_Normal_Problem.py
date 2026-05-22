n = int(input())

for _ in range(n): 
    s = input()[::-1]
    out = ''
    for i in s : 
        if i == 'q' : 
            out += 'p'
        elif i =='p' : 
            out += 'q'
        else : 
            out += 'w'
    print(out)