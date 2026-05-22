x= int(input())

for _ in range(x) : 
    n = int(input())
    grid = []
    for i in range(n) : 
        grid.append(list(map(int,input().split())))
    permutation = [0] * 2*n
    for i in range(n) : 
        for j in range(n) : 
            permutation[i+j+1] = grid[i][j]
    
    permutation[0] = sum(range(1,2*n+1)) - sum(permutation)
    
    print(*permutation)