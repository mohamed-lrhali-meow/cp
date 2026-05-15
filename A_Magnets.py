n = int(input())
magnets = []
c = 1
for _ in range(n): 
    magnets.append(int(input()))
for i in range(len(magnets)-1): 
    if magnets[i] != magnets[i+1]: 
        c +=1 

print(c)
