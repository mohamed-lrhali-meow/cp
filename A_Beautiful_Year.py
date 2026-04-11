n = int(input())
n +=1
while True : 
    if 4 == len(set(str(n))) : 
        print(n)
        break
    else: 
        n+=1
