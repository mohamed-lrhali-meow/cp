n = int(input())

for _ in range(n) : 
    x = int(input())
    cells = input()
    print(2) if "..." in cells else print(cells.count("."))